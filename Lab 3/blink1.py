import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
n=0
#while (n<10):
    #num=int(input("enter a number"))
    #GPIO.output(18,True)
    #time.sleep(1)
    #GPIO.output(18,False)
    #time.sleep(1)
    #n=n+1

GPIO.output(18,True)
time.sleep(1)
GPIO.output(18,False)
time.sleep(1)
GPIO.output(18,True)
time.sleep(1)
GPIO.output(18,False)
GPIO.output(23,True)
time.sleep(1)
GPIO.output(23,False)
time.sleep(1)
GPIO.output(23,True)
time.sleep(1)
GPIO.output(23,False)
GPIO.output(25,True)
time.sleep(1)
GPIO.output(25,False)
time.sleep(1)
GPIO.output(25,True)
time.sleep(1)
GPIO.output(25,False)
