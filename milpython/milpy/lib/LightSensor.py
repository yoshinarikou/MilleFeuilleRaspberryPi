#!/usr/bin/python

import spidev
from ..mil import p
import time
from ..mil import wiringdata

#ADspibus = spidev.SpiDev()
ADspibus = spidev.SpiDev(0,1)
#AD2spibus.max_speed_hz = 1200000
moduleAddress1 = 0x8000
moduleAddress2 = 0x000D
moduleAddress = 0x8000000D


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
	IOdata = wiringdata.getWiring(moduleAddress)

	return IOdata
	

def read(milModClass):

	ioData = getIOs()
	#print "ioData = ",ioData
	wiringdata.IOout(milModClass.pinData[0],1)#CS High
	ADspibus.max_speed_hz = 20000000
	ADspibus.xfer2([0xFF,0xFF, 0]) #Test Send
	
	ADspibus.mode = 3
	ADspibus.max_speed_hz = 4000000
	wiringdata.IOout(milModClass.pinData[0],0)#CS low
	reData = ADspibus.xfer2([0x00, 0x00])
	#print "reData = ",reData
	#reply = ((reData[0] << 8)+reData[1])
	reply = ((reData[0] << 7)+(reData[1]>>1))
	wiringdata.IOout(milModClass.pinData[0],1)#CS High
	
	return reply
	


def test(milModClass):
	ioData = getIOs()
	print "ioData = ",ioData
	wiringdata.IOout(ioData[0],1)#CS High
	wiringdata.IOout(milModClass.pinData[0],1)
	time.sleep(0.1)
	wiringdata.IOout(ioData[0],0)#CS low
	wiringdata.IOout(milModClass.pinData[0],0)
	time.sleep(0.1)

def cleanup():
	ADspibus.close()
	
	
