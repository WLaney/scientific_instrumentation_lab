import RPi.GPIO as GPIO
import time


#pin defenition
left=17 #turn rotary switch left
right=27 #turn rotary switch right
#Please note that left and right are arbitrary and there reversal does not matter


#pin swt up
GPIO.setmode(GPIO.BCM)
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#inital variables
global num
num=0
count=5

#if turn to the left increase count
def ISR_left(pin):
    global num
    if num==0:
       num=1


#if turn to right decrease count
def ISR_right(pin):
    global num
    if num==0:
       num=-1




#use interupts to see rotatry switch direction
GPIO.add_event_detect(left, GPIO.FALLING, callback=ISR_left, bouncetime=100)
GPIO.add_event_detect(right, GPIO.FALLING, callback=ISR_right, bouncetime=100)



try: #set up keyboard exception
   while (True):
        if num ==1:
            count += 1
            print(count)
            num=0
        elif num == -1:
            count -= 1
            print(count)
            num=0
        else:
            x=1
        
except KeyboardInterrupt:
      GPIO.cleanup()


