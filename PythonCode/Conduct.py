import RPi.GPIO as gpio
import copy

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
xservo = gpio.PWM(dic[18], 50)
xservo.start(6.5)

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

pre_stack = []

def setStack(stack):
    global pre_stack
    pre_stack = copy.deepcopy(stack)    #깊은 복사

def conduct(stack):
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
    gpio.cleanup()
            
if __name__ == "__main__":
    print("test code")
    setStack([1,1,2,2,3,3,4])
    print ("pre : ", pre_stack)
