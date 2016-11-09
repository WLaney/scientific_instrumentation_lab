import smbus
import time
import sys

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
DEVICE_ADDRESS = 0x39#7 bit address (will be left shifted to add the readwrite bit)
set_gain = 0x81 #1x gain, 101ms 0x01. 16x gain, 101ms 0x11

gain_low=0x01 #1x gain, 101ms
gain_high=0x11 #16x gain, 101ms
read_ch0 = 0xAC #visable and ir
read_ch1=0xAE #only ir
#if this dosent work try shifting bit 7 by 1, ie 0x02, 0x012, 0x8C, 0x8E

#write_i2c_block_data(DEVICE_ADRESS,0x80, 0x03) #enable the device

while True:
    
    #read chanel 0
    ch0=bus.read_i2c_block_data(DEVICE_ADDRESS, read_ch0)
    print("ch0 value:" ch0)

    #read chanel 1
    ch1=bus.read_i2c_block_data(DEVICE_ADDRESS, read_ch1)
    print("ch1 value:" ch1)

    #convert reading to lux
    ratio=ch1/ch2

    if ( 0 <= ratio <=. 50):
        lux=0.0304*ch0-0.0593*ch0*(ratio^(1.4))
    elif ( 0.5 < ratio <= 0.61):
        lux=0.0224*ch0-0.031*ch1
    elif ( 0.61 < ratio <=0.80):
        lux=0.0128*ch0-0.0153*ch1
    elif ( 0.80 < ratio <= 1.30):
        lux=0.00146*ch0-0.00112*ch1
    else:
        lux=0

    print(lux)

    time.sleep(5)

    
    
