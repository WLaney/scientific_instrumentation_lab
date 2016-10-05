import RPi.GPIO as GPIO
import time

#pin defenition
left=17 #turn rotary switch left
right=27 #turn rotary switch right
#Please note that left and right are arbitrary and there reversal does not matter

#pin swt up
GPIO.setmode(GPIO.BCM)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)

#inital variables
num=5.0

try: #set up keyboard exception
   while (True):
       #use interupts to see rotatry switch direction
       GPIO.add_event_detect(left, GPIO.RISING, callback=ISR_left, bouncetime=50)
       GPIO.add_event_detect(right, GPIO.RISING, callback=ISR_right, bouncetime=50)

except KeyboardInterrupt:
      GPIO.cleanup()

#if turn to the left increase count
def ISR_left(pin):
    if num < 10:
        num += 0.5

#if turn to right decrease count
def ISR_right(pin):
    if num > 0:
        num -= 0.5
