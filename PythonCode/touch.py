import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
count = 0

while(True):
   # st = input("on:t / exit:e  :  ")
   # direction = st[0]
   # if direction == "t":
        GPIO.setup(24,GPIO.OUT)
        GPIO.output(24, 1)
        time.sleep(0.2)
        GPIO.setup(24, GPIO.IN)
        GPIO.input(24)
        time.sleep(0.2)
        
        
        count+=1
        print(count)
        if count == 20:
            break
   # elif direction == "e":        
   #     break
GPIO.cleanup()
