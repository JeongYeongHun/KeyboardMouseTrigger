import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#ser.open()

test = "abcdafafafafafafafafafafafafafafdsdsds1"

    


while True:
    ser.write(test.encode())
    time.sleep(1)
    if ser.readable():
        res = ser.readline()
        print(res.decode())
