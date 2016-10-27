#!/usr/bin/python2.7

import smbus
import time
import numpy as np
# After running sudo 12cdetect - y 1 and finding an address, you know to use channel 1
bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
# After running sudo 12cdetect - y 1 the address should be 0x60 (Hex 60)
DEVICE_ADDRESS = 0x60      #7 bit address (will be left shifted to add the read write bit)
# To write to normal memory, use command 0x40
DEVICE_REG_OUT = 0x40
# To write to persistent memory (EEPROM), use command 0x60
# The DAC will then remember the value after powering off

def square(t,T):
    return 4095*(int(2*t/T) % 2)

def sin(t,T):
    return 2048 + int(2047*np.sin(2*np.pi*t/T))

def make_vals(func,T):
    return [func(t,T) for t in range(T)]

def write_per(l):
    for val in l:
        reg_data = [(val >> 4) & 0xFF, (val << 4) & 0xFF]
        bus.write_i2c_block_data(DEVICE_ADDRESS,
                                 DEVICE_REG_OUT, reg_data)

output = make_vals(sin,128)
print output
while(True):
    try:
        while(True):
            write_per(output)
    except KeyboardInterrupt:
        output = make_vals(sin,input("Period?\n"))
        print output
        
## try:
##     while(True):
##         value = 0
## # Step through a set of values
##         while (value< 2048):
##             value += 100
## # Note that value MUST be an integer from 0 to 2047
##             reg_data = [(value >> 4) & 0xFF, (value << 4) & 0xFF]
## #Write an array of registers
##             bus.write_i2c_block_data(DEVICE_ADDRESS,
##                                      DEVICE_REG_OUT, reg_data)
## except KeyboardInterrupt:
##     time.sleep(.01)
