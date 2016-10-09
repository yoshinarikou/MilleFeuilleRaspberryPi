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
import spidev
from ..mil import p
from ..mil import wiringdata

AD2spibus = spidev.SpiDev()
AD2spibus = spidev.SpiDev(0,1)
#AD2spibus.max_speed_hz = 1200000
moduleAddress1 = 0x8000
moduleAddress2 = 0x0005
moduleAddress = 0x80000005

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
	

def read(milModClass, ch):

	#ioData = getIOs()
	#wiringdata.IOout(ioData[3],1)#CS High
	wiringdata.IOout(milModClass.pinData[3],1)#CS High
	AD2spibus.max_speed_hz = 20000000
	AD2spibus.xfer2([0xFF,0xFF, 0]) #Test Send
	
	if ch == 0:
		cmd = 0x80
	elif ch == 1:
		cmd = 0xC0
	
	AD2spibus.max_speed_hz = 1000000
	#wiringdata.IOout(ioData[3],0)#CS low
	wiringdata.IOout(milModClass.pinData[3],0)#CS low
	reData = AD2spibus.xfer2([0x01,cmd, 0])
	reply = ((reData[1] << 8)+reData[2]) - 0xE000
	#wiringdata.IOout(ioData[3],1)#CS High
	wiringdata.IOout(milModClass.pinData[3],1)#CS High
	
	return reply
	
def cleanup():
	AD2spibus.close()
