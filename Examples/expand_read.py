#!/usr/bin/python


import spidev
import time

read = 0

spi = spidev.SpiDev()
spi.open(1,0)  # /dev/spidev1.0

#Check the states for 16 bits
def read():
		print spi.readbytes(16)
		
	
read()

spi.close