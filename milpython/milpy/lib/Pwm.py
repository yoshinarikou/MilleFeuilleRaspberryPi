########################################################################
#	MCU Gear(R) system Sample Code
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	8/OCT/2016
#
########################################################################
#Revision Information
#
########################################################################

#!/usr/bin/python
from ..mil import mil
import smbus
from ..mil import p
from ..mil import wiringdata
import time


i2c=smbus.SMBus(1)

#I2C_address = 0x40
I2C_address = 0x6A
PCA9685_MODE1 = 0x00
PCA9685_PRESCALE = 0xFE
LED0_ON_L = 0x06
LED0_ON_H = 0x07
LED0_OFF_L = 0x08
LED0_OFF_H = 0x09

moduleAddress1 = 0x8000
moduleAddress2 = 0x0015
moduleAddress = 0x80000015

def getInfo(Number):
	if ((Number >= 0) and (Number <= 3)):
		address = moduleAddress + Number
		address2 = moduleAddress2 + Number
		address1 = moduleAddress1
		#check address
		testaddr = (address1<<16) + address2
		if address != testaddr:
			print "ERROR: Device address is not correct!"
			address1 = -1
			address2 = -1
			
	else:
		address = -1
	
	IOdata = wiringdata.getWiring(address)
	datas = [address1,address2]
	datas.extend(IOdata)
	return datas

def getAddr(Number):
	address = -1
	if ((Number >= 0) and (Number <= 3)):
		address = moduleAddress2 + Number
	else:
		address = -1

	return moduleAddress1,moduleAddress2

def getIOs():
	#IOdata = [p.CE1]
	#print "moduleAddress =",moduleAddress 
	IOdata = wiringdata.getWiring(moduleAddress)

	return IOdata


def setPwm(t_num, on, off):
	cmd = [0,0,0,0]
	regCmd = LED0_ON_L + 4 * t_num
	#print "regCmd = ",regCmd
	#regCmd = 0x00
	#cmd[0] = (on & 0xff)
	cmd[0] = on
	#cmd[1] = ((on >> 8) & 0xff)
	cmd[1] = (on >> 8)
	#cmd[2] = (off & 0xff)
	cmd[2] = off
	#cmd[3] = ((off >> 8) & 0xff)
	cmd[3] = (off >> 8)
	i2c.write_i2c_block_data(I2C_address, regCmd, cmd)
	

def setServoPulse(n,pulse):
	setPwm(n, 0, pulse)
	
	

def initPwm():
	i2c.write_byte_data(I2C_address, PCA9685_MODE1,0x00)
	oldmode = i2c.read_byte_data(I2C_address, PCA9685_MODE1)
	#print "oldmode = ", oldmode
	newmode = ((oldmode & 0x7F)|0x10)
	#print "newmode = ", newmode
	i2c.write_byte_data(I2C_address, PCA9685_MODE1,newmode)
	time.sleep(0.01)
	i2c.write_byte_data(I2C_address, PCA9685_PRESCALE,121)
	i2c.write_byte_data(I2C_address, PCA9685_MODE1,oldmode)
	time.sleep(0.01)
	i2c.write_byte_data(I2C_address, PCA9685_MODE1,(oldmode | 0xa1))
	#print "(oldmode | 0xa1) = ", (oldmode | 0xa1)
	

	
def cleanup():
	i2c.close()
