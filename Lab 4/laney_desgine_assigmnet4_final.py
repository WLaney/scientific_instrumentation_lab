import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
BTN1 = 17 # Broadcom pin 17 (P1 pin 11)
BTN2 = 27 # Broadcom pin 27 (P1 pin 13)

# Pin setups:
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(BTN1, GPIO.IN)
GPIO.setup(BTN2, GPIO.IN)

# Button pin set as input w/ pull-up
GPIO.setup(BTN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize PWM on pwmPin at 100hz
pwm = GPIO.PWM(pwmPin, 100)

# Start at duty cycle of 50%
num=10
# Start PWM
pwm.start(num)

#define hwo much button changes duty cycle by
change=5

#begin an infinte loop to check for button press
while True:
    if (not GPIO.input(BTN1) and not GPIO.input(BTN2)):# if both buttons presse
        time.sleep(0.1) #wait then check if buttons are still presed
        if (not GPIO.input(BTN1) and not GPIO.input(BTN2)): #this helps debounce
            print("exit")
            break
        
    elif (not GPIO.input(BTN1)): #check if button 1 is pressed 
        time.sleep(0.1) #wait then check if button is still presed
        if (not GPIO.input(BTN1)):#this helps debounce
            print("button 1")
            if (num<100): #the udty cycle can not go over 100
                num=num+change #incease the duty cycle
                pwm.ChangeDutyCycle(num)
            print(num)
        
    elif (not GPIO.input(BTN2)): #check if button 2 is pressedd
        time.sleep(0.1) #wait then check if button is still presed
        if (not GPIO.input(BTN2)):#this helps debounce
            print("button 2")
            if (num>0): #the duty cycle can no go under 0
                num=num-change #decrease the duty cycle
                pwm.ChangeDutyCycle(num)
            print(num)

           
    else: #if no button pressed wait 1ms and check again
        time.sleep(0.01)

GPIO.cleanup()
        
    
  
