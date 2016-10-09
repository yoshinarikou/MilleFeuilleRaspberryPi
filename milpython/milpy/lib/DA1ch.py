##################################################################################################################
#	MCU Gear(R) Sample Code
#	Auther:y.kou.
#	web site: http://www.mille-feuille.mcugear.com/
#	Date	:	30/7/2015
##################################################################################################################
#Revision Information
#
##################################################################################################################

#!/usr/bin/python
from ..mil import mil
import spidev
from ..mil import p
from ..mil import wiringdata
import time

DAspibus = spidev.SpiDev(0,1)
#DAspibus.max_speed_hz = 2000000
moduleAddress1 = 0x8000
moduleAddress2 = 0x0009
moduleAddress = 0x80000009

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

	#print "address =",hex(address) 
	#print "moduleAddress =",hex(moduleAddress) 
	#print "Number =",Number 

	#myAddress = address

	return moduleAddress1,moduleAddress2

def getIOs():
	#IOdata = [p.CE1]
	#print "moduleAddress =",moduleAddress 
	IOdata = wiringdata.getWiring(moduleAddress)

	return IOdata
	


def write(milModClass,data):
	#print "data = ",data
	#mil.IO(p.outpin[0],True)
	#time.sleep(0.0001)

	wiringdata.IOout(milModClass.pinData[1],1)#CS High
	wiringdata.IOout(milModClass.pinData[3],1)#LDAC High
	DAspibus.max_speed_hz = 20000000
	DAspibus.xfer2([0xFF,0xFF, 0]) #Test Send
	
	wiringdata.IOout(milModClass.pinData[1],0)#CS Low
	DAspibus.max_speed_hz = 20000000

	sendData = 0x30 + ((data >> 8) & 0x0f)
	sendData2 = data & 0xff
	
	reData = DAspibus.xfer2([sendData,sendData2])
	
	wiringdata.IOout(milModClass.pinData[1],1)#CS High
	time.sleep(0.000000015)
	wiringdata.IOout(milModClass.pinData[3],0)#LDAC Low
	time.sleep(0.0000001)
	wiringdata.IOout(milModClass.pinData[3],1)#LDAC High

	#time.sleep(0.0001)
	#mil.IO(p.outpin[0],False)
	
def cleanup():
	DAspibus.close()

	
