import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

# Direction pin from controller|
DIR = 21
# Step pin from controller
STEP = 20
# 0/1 used to signify clockwise or counterclockwise.

CW = 1
CCW = 0

# Setup pin layout on PI
GPIO.setmode(GPIO.BCM)

# Establish Pins in software
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Set the first direction you want it to spin
GPIO.output(DIR, CW)


def motorDer():
    sleep(1)
    GPIO.output(DIR,CCW)
    sleep(.5)
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        sleep(0.00045)
        GPIO.output(STEP, GPIO.LOW)
        sleep(0.00045) # Dictates how fast stepper motor will run
        
def prueba():
    sleep(1)
    GPIO.output(DIR,CCW)
    sleep(.5)
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        sleep(0.0008)
        GPIO.output(STEP, GPIO.LOW)
        sleep(0.0008) # Dictates how fast stepper motor will run
        
        
        
def motorIzq():
    sleep(1)
    
    #Establish the direction you want to go
    GPIO.output(DIR,CW)
    vueltas = 50*200
    velocidad = 0.0006
    for x in range(vueltas):
        if(x < 1200 or x > vueltas - 1200):
            velocidad = 0.0006 #Vamos lento al principio y  al final
        else:
            velocidad = 0.0004 #Vamos rapido en el medio

        GPIO.output(STEP, GPIO.HIGH)
        sleep(velocidad)
        GPIO.output(STEP, GPIO.LOW)
        sleep(velocidad) # Dictates how fast stepper motor will run
    
    
        
prueba()
    
    
    
    
    
    
    
    
    
    
    
    
    
    