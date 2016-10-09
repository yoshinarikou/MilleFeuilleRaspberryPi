
#!/usr/bin/python
from ..mil import mil
import spidev
from ..mil import p
from ..mil import wiringdata

AD2spibus = spidev.SpiDev()
AD2spibus = spidev.SpiDev(0,1)
#AD2spibus.max_speed_hz = 1200000
moduleAddress1 = 0xC000
moduleAddress2 = 0x0001
moduleAddress = 0xC0000001

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
	
