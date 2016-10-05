import spidev # import SPI development module
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

#pin swt up
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def bitstring(n):  # function to extract bytes from ADC
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s

def start(y):
    global st
    st=1

conn = spidev.SpiDev(0, 0) # establish connection to ADC
conn.max_speed_hz = 1000000 #1.0 Mhz
conn.mode = 0
cmd = 192 #start bit + single ended

n=0
y=[0]*1000
x=[0]*1000
global st
st=0
GPIO.add_event_detect(17, GPIO.RISING, callback=start, bouncetime=100)
try:
    while (True):
        if st==1:
            print "start data"
            while n<1000:
                reply_bytes = conn.xfer2([cmd, 0]) # sends command to start conversion and reply
                reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
                reply = reply_bitstring[5:15] # take only 10 bits
                #print int(reply, 2)*3.3/2**10 #generate voltage
                y[n]=int(reply, 2)*3.3/2**10
                n += 1
            break
        else:
            h=0
    x=range(0,1000,1) 
    plt.plot(x, y)
    plt.show()
    
        

except KeyboardInterrupt:
    GPIO.cleanup()
    conn.close()
