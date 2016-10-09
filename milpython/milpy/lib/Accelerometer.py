########################################################################
#	MCU Gear(R) system Sample Code
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	8/OCT/2016
#
#      ------ATTENTION------
#  "If you want to use this library, you need these command."
#  $sudo chmod 666 /sys/module/i2c_bcm2708/parameters/combined
#  $sudo echo -n 1 >  /sys/module/i2c_bcm2708/parameters/combined
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

#I2C_address = 0x0D
I2C_address = 0x1C

moduleAddress1 = 0x8000
moduleAddress2 = 0x003D
moduleAddress = 0x8000003D

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

def get_acc(axis):
	
	res = [0,0]
	#print "axis = ",axis
	
	Data = i2c.read_word_data(I2C_address, axis)
	#print "acc = ",hex(Data)
	res[0] = Data & 0x00FF
	res[1] = (Data & 0xFF00) >> 8 
	#print "res[0] = ",hex(res[0])
	#print "res[1] = ",hex(res[1])
	acc = (res[0] << 6) | (res[1] >> 2)
	if acc > (16383 / 2):
		acc -= 16383
		
	acc = acc/4096.0
	#print "acc x = ",acc
	return acc
	

def get_X():
	accX = get_acc(0x01)
	#print "accX = ",accX
	return accX
	
def get_Y():
	accY = get_acc(0x03)
	#print "accY = ",accY
	return accY
	
def get_Z():
	accZ = get_acc(0x05)
	#print "accZ = ",accZ
	return accZ
	

def init():
	
	i2c.write_byte_data(I2C_address, 0x2A,0x01)
	ID = i2c.read_byte_data(I2C_address, 0x0D)
	print "ID = ",ID
	#time.sleep(0.01)
	return ID

	
def cleanup():
	i2c.close()
