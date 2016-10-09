##################################################################################################################
#	MCU Gear(R) Sample Code
#	Auther:y.kou.
#	web site: http://www.mille-feuille.mcugear.com/
#	Date	:	30/7/2015
##################################################################################################################
#Revision Information
#
##################################################################################################################
#Hardware IO data
#MGminiModule.MGminiModule(3,p.CE1)
##################################################################################################################

#!/usr/bin/python
from ..mil import mil
#import smbus
from ..mil import p
from ..mil import wiringdata
import time
import struct, array, time, io, fcntl

I2C_address = 0x40
TEMP = 0x00
HUMIDITY = 0x01
CONF = 0x02
MANUID= 0xFE
DEVICEID= 0xFF

moduleAddress1 = 0x8000
moduleAddress2 = 0x0021
moduleAddress = 0x80000021


I2C_SLAVE=0x0703

bus=1
fr = io.open("/dev/i2c-"+str(bus), "rb", buffering=0)
fw = io.open("/dev/i2c-"+str(bus), "wb", buffering=0)

# set device address
fcntl.ioctl(fr, I2C_SLAVE, I2C_address)
fcntl.ioctl(fw, I2C_SLAVE, I2C_address)
time.sleep(0.015) #15ms startup time


def getInfo():
	Number = 0
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


def init():
	s = [0x02,0x00,0x00]
	s2 = bytearray( s )
	fw.write( s2 ) #sending config register bytes
	time.sleep(0.015)               # From the data sheet

def readTemp():
	
	s = [0x00] # temp
	s2 = bytearray( s )
	fw.write( s2 )
	time.sleep(0.0625)              # From the data sheet

	data = fr.read(2) #read 2 byte temperature data
	buf = array.array('B', data)
	rawData = ((buf[0]<<8) + (buf[1]))
	Temp = (((rawData/65536.0)*165.0 ) - 40.0) 

	time.sleep(0.015)               # From the data sheet
	return Temp,rawData
	
def readHumidity():
	
	s = [0x01] # hum
	s2 = bytearray( s )
	fw.write( s2 )
	time.sleep(0.0625)              # From the data sheet

	data = fr.read(2) #read 2 byte temperature data
	buf = array.array('B', data)
	rawData = ((buf[0]<<8) + (buf[1]))
	Humidity = ((rawData/65536.0)*100.0 ) 
	return Humidity, rawData
	
def cleanup():
	i2c.close()
