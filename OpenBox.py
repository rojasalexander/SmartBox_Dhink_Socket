import RPi.GPIO as GPIO
import time

channel = 21
channel2 = 20
channel3 = 16
channel4 = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setup(channel, GPIO.OUT) # GPIO Assign mode
GPIO.setup(channel2, GPIO.OUT) # GPIO Assign mode
GPIO.setup(channel3, GPIO.OUT) # GPIO Assign mode
GPIO.setup(channel4, GPIO.OUT) # GPIO Assign mode
#IMPORTANTE, setear cada locker a HIGH cuando empiece el programa
GPIO.output(channel, GPIO.HIGH)
GPIO.output(channel2, GPIO.HIGH)
GPIO.output(channel3, GPIO.HIGH)
GPIO.output(channel4, GPIO.HIGH)

def abrirCaja(pin, i):
    print("abrir la caja nro: ", i)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)

def cajaNro(index):
    if(index == 1):
        abrirCaja(channel, 1)
    elif(index == 2):
        abrirCaja(channel2, 2)
    elif(index == 3):
        abrirCaja(channel3, 3)
    elif(index == 4):
        abrirCaja(channel4, 4)
