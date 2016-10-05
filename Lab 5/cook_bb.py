import spidev # import SPI development module
import time

import matplotlib.pyplot as plt


def bitstring(n):  # function to extract bytes from ADC
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s

conn = spidev.SpiDev(0, 0) # establish connection to ADC
conn.max_speed_hz = 1000000 #1.0 Mhz
conn.mode = 0
cmd = 192 #start bit + single ended

n=0


try:
    while n<1000:
        reply_bytes = conn.xfer2([cmd, 0]) # sends command to start conversion and reply
        reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
        reply = reply_bitstring[5:15] # take only 10 bits
        print int(reply, 2)*3.3/2**10 #generate voltage
        time.sleep(.1)
        n += 1
        
    plt.plot(x, y)
    plt.show()
        

except KeyboardInterrupt:
    conn.close()
