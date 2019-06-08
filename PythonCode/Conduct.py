import RPi.GPIO as gpio
#from RPIO import PWM
import copy
import time

dic = {0:26, 1:24, 2:26, 3:24, 4:26, 5:22, 6:21, 7:20, 8:16, 9:23, 10:6, 11:5, 12:11, 13:9, 14:10, 16:7, 17:8, 18:18, 19:19}

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(dic[1], gpio.OUT)
adservo = gpio.PWM(dic[1], 50)
adservo.start(6.5)

gpio.setup(dic[0], gpio.OUT)
wsservo = gpio.PWM(dic[0], 50)
wsservo.start(6.5)

gpio.setup(dic[18], gpio.OUT)
x = 7
xservo = gpio.PWM(dic[18], 50)
xservo.start(x)

gpio.setup(dic[19], gpio.OUT)
yservo = gpio.PWM(dic[19], 50)
yservo.start(6.5)

gpio.setup(dic[5], gpio.OUT)
gpio.setup(dic[6], gpio.OUT)
gpio.setup(dic[7], gpio.OUT)
gpio.setup(dic[8], gpio.OUT)
gpio.setup(dic[9], gpio.OUT)
gpio.setup(dic[10], gpio.OUT)
gpio.setup(dic[11], gpio.OUT)
gpio.setup(dic[12], gpio.OUT)
gpio.setup(dic[13], gpio.OUT)
gpio.setup(dic[14], gpio.OUT)
gpio.setup(dic[16], gpio.OUT)
gpio.setup(dic[17], gpio.OUT)

gpio.setup(17, gpio.OUT) #touchBar

pre_stack = []
tBar = True
gpio.output(17, tBar)

def setStack(stack):
    global pre_stack
    pre_stack = copy.deepcopy(stack)    #깊은 복사

def conduct(stack):
    if stack[18] != 0:
        global x
        global tBar
        x = round(x,2)
        omx = x - 5
        
        if tBar:
            mx = omx + (stack[18]/10)
        elif not tBar:
            mx = omx - (stack[18]/10)

        move = abs(stack[18]/10)
        
        if mx > 4:
            if tBar:    #move right
                print ("  case 1. ")
                xservo.ChangeDutyCycle(9.0)
                time.sleep(0.3)
                move = round(move - (4 - omx),2)
                tBar = not tBar
                gpio.output(17, tBar)
                while move > 4:
                    if tBar:
                        xservo.ChangeDutyCycle(9.0)
                    else:
                        xservo.ChangeDutyCycle(5.0)
                    time.sleep(0.3)
                    move = move - 4
                    tBar = not tBar
                    gpio.output(17, tBar)
                if tBar:
                    x = 5.0+move
                elif not tBar:
                    x = 9.0-move
                xservo.ChangeDutyCycle(x)
                time.sleep(0.2)
            elif not tBar:  #move left
                print ("  case 2. ")
                xservo.ChangeDutyCycle(9.0)
                time.sleep(0.3)
                move = round(move - (4 - omx),2)
                tBar = not tBar
                gpio.output(17, tBar)
                while move > 4:
                    if tBar:
                        xservo.ChangeDutyCycle(5.0)
                    else:
                        xservo.ChangeDutyCycle(9.0)
                    time.sleep(0.3)
                    move = move - 4
                    tBar = not tBar
                    gpio.output(17, tBar)
                if tBar:
                    x = 9.0-move
                elif not tBar:
                    x = 5.0+move
                xservo.ChangeDutyCycle(x)
                time.sleep(0.2)
        elif mx < 0:
            if tBar:    #move left
                print ("  case 3. ")
                xservo.ChangeDutyCycle(5.0)
                time.sleep(0.3)
                move = round(move - omx,2)
                tBar = not tBar
                gpio.output(17, tBar)
                while move > 4:
                    if tBar:
                        xservo.ChangeDutyCycle(5.0)
                    else:
                        xservo.ChangeDutyCycle(9.0)
                    time.sleep(0.3)
                    move = move - 4
                    tBar = not tBar
                    gpio.output(17, tBar)
                if tBar:
                    x = 9.0-move
                elif not tBar:
                    x = 5.0+move
                xservo.ChangeDutyCycle(x)
                time.sleep(0.2)
            elif not tBar:  #move right
                print ("  case 4. ")
                xservo.ChangeDutyCycle(5.0)
                time.sleep(0.3)
                move = round(move - omx,2)
                tBar = not tBar
                gpio.output(17, tBar)
                while move > 4:
                    if tBar:
                        xservo.ChangeDutyCycle(9.0)
                    else:
                        xservo.ChangeDutyCycle(5.0)
                    time.sleep(0.3)
                    move = move - 4
                    tBar = not tBar
                    gpio.output(17, tBar)
                if tBar:
                    x = 5.0+move
                elif not tBar:
                    x = 9.0-move
                xservo.ChangeDutyCycle(x)
                time.sleep(0.2)
        else:
            xservo.ChangeDutyCycle(mx+5)
            x = mx+5
            time.sleep(0.2)
            print ("  x : ", x)
                

    for index, i in enumerate(stack):   #compare
        if pre_stack[index] != i:
            if i == 0:  #key up
                if index < 5 or index == 18 or index == 19: #servo motor
                    if index == 0 and pre_stack[2] == 0:    #w
                        wsservo.ChangeDutyCycle(6.5)
                    elif index == 2 and pre_stack[0] == 0:  #s
                        wsservo.ChangeDutyCycle(6.5)
                    elif index == 0 and pre_stack[2] == 1:
                        wsservo.ChangeDutyCycle(5.0)
                    elif index == 2 and pre_stack[0] == 1:
                        wsservo.ChangeDutyCycle(8.0)
                    if index == 1 and pre_stack[3] == 0:    #a
                        adservo.ChangeDutyCycle(6.5)
                    elif index == 3 and pre_stack[1] == 0:  #d
                        adservo.ChangeDutyCycle(6.5)
                    elif index == 1 and pre_stack[3] == 1:
                        adservo.ChangeDutyCycle(5.0)
                    elif index == 3 and pre_stack[1] == 1:
                        adservo.ChangeDutyCycle(8.0)
                else:
                    gpio.output(dic[index], 0)
            if i == 1:  #key down
                if index < 4 or index == 18 or index == 19: #servo motor
                    if index == 0 and pre_stack[2] == 0:    #w
                        wsservo.ChangeDutyCycle(8.0)
                    elif index == 2 and pre_stack[0] == 0:  #s
                        wsservo.ChangeDutyCycle(5.0)
                    if index == 1 and pre_stack[3] == 0:    #a
                        adservo.ChangeDutyCycle(8.0)
                    elif index == 3 and pre_stack[1] == 0:  #d
                        adservo.ChangeDutyCycle(5.0)
                else: 
                    gpio.output(dic[index], 1)
    setStack(stack)

def endConduct():
    adservo.stop()
    wsservo.stop()
    xservo.stop()
    gpio.cleanup()
            
if __name__ == "__main__":
    print("test code")
    setStack([1,1,2,2,3,3,4])
    print ("pre : ", pre_stack)

''' #Before Mouse Moving Code
        if tBar:
            mx = x + (stack[18] / 10)
        if not tBar:
            mx = x + ((stack[18] / 10) *(-1))
        
        if mx > 9 or mx < 5:
            if mx > 9 and tBar:
                print ("case 1.")
                xservo.ChangeDutyCycle(9.0)
                time.sleep(0.3)
                mx = mx - 9
                mcycle = mx // 4
                for i in range(int(mcycle), 0, -1):
                    tBar = not tBar
                    gpio.output(17, tBar)
                    if not tBar:
                        xservo.ChangeDutyCycle(5.0)
                    if tBar:
                        xservo.ChangeDutyCycle(9.0)
                    time.sleep(0.3)
                tBar = not tBar
                gpio.output(17, tBar)
                if tBar:
                    x = mx - (mcycle*4) + 5
                if not tBar:
                    x = 9 - (mx - (mcycle*4))
                xservo.ChangeDutyCycle(round(x,2))
                time.sleep(0.3)
            elif mx > 9 and not tBar:
                print ("case 2.")
                xservo.ChangeDutyCycle(5.0)
                time.sleep(0.3)
                mx = mx - (x-5) -x
                mcycle = mx // 4
                for i in range(int(mcycle), 0, -1):
                    tBar = not tBar
                    gpio.output(17, tBar)
                    if not tBar:
                        xservo.ChangeDutyCycle(5.0)
                    if tBar:
                        xservo.ChangeDutyCycle(9.0)
                    time.sleep(0.3)
                tBar = not tBar
                gpio.output(17, tBar)
                if tBar:
                    x = mx - (mcycle*4) + 5
                if not tBar:
                    x = 9 - (mx - (mcycle*4))
                xservo.ChangeDutyCycle(round(x,2))
                time.sleep(0.3)
            elif mx < 5 and tBar:
                print ("case 3.")
                xservo.ChangeDutyCycle(5.0)
                time.sleep(0.3)
                mx = x - mx - (x-5)
                mcycle = mx // 4
                for i in range(int(mcycle), 0, -1):
                    tBar = not tBar
                    gpio.output(17, tBar)
                    if not tBar:
                        xservo.ChangeDutyCycle(9.0)
                    if tBar:
                        xservo.ChangeDutyCycle(5.0)
                    time.sleep(0.3)
                tBar = not tBar
                gpio.output(17, tBar)
                if not tBar:
                    x = mx - (mcycle*4) + 5
                if tBar:
                    x = 9 - (mx - (mcycle*4))
                xservo.ChangeDutyCycle(round(x,2))
                time.sleep(0.3)
            elif mx < 5 and not tBar:
                print ("case 4.")
                xservo.ChangeDutyCycle(9.0)
                time.sleep(0.3)
                mx = x - mx - (9-x)
                mcycle = mx // 4
                for i in range(int(mcycle), 0, -1):
                    tBar = not tBar
                    gpio.output(17, tBar)
                    if not tBar:
                        xservo.ChangeDutyCycle(9.0)
                    if tBar:
                        xservo.ChangeDutyCycle(5.0)
                    time.sleep(0.3)
                tBar = not tBar
                gpio.output(17, tBar)
                if not tBar:
                    x = mx - (mcycle*4) + 5
                if tBar:
                    x = 9 - (mx - (mcycle*4))
                xservo.ChangeDutyCycle(round(x,2))
                time.sleep(0.3)
        else:
            xservo.ChangeDutyCycle(round(mx,2))
            x = round(mx,2)

        print("x : ", x)
'''    
