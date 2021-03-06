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
from ..mil import p
from ..mil import wiringdata

moduleAddress1 = 0x8000
moduleAddress2 = 0x0029
moduleAddress = 0x80000029

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
	
def power(milModClass, OnOff):
	wiringdata.IOout(milModClass.pinData[0],OnOff)

def read(milModClass):
	return wiringdata.IOin(milModClass.pinData[1])


def holdConnect(milModClass):
	milModClass.connect() #connect before Hold off
	milModClass.HoldOff() #hold but not connect

def holdDisconnect(milModClass):
	milModClass.HoldOn(0x01)
	#milModClass.disconnect() #connect before Hold off
	milModClass.cutWire()
