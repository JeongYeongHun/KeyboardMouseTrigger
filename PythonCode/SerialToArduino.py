import serial
import time
ser = serial.Serial('/dev/ttyACM0', 115200)

def sendserial(stack):
    key = ""
    for s in stack:
        key = key + " " + repr(s)
    ser.write(key.encode())
#    if ser.readable():
#        res = ser.readline()
#        print(res.decode())
