#!/usr/bin/env python3
import serial
import time
                
def abrir():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        for x in range(2):        
            ser.write(b"ABRIR\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
        
        
def cerrar():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        for x in range(2):        
            ser.write(b"CERRAR\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)

        