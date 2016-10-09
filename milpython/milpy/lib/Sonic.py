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
from ..mil import p
from ..mil import wiringdata
import time

moduleAddress1 = 0x8000
#moduleAddress2 = 0x0001
#moduleAddress = 0x80000001
moduleAddress2 = 0x0019
moduleAddress = 0x80000019

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
	
	
def read(milModClass,mode):

	if mode == 0:
		for var in range(0,5):
			wiringdata.IOout(milModClass.pinData[0],1)
			wiringdata.IOout(milModClass.pinData[0],1)
			wiringdata.IOout(milModClass.pinData[0],1)
			wiringdata.IOout(milModClass.pinData[0],0)
			wiringdata.IOout(milModClass.pinData[0],0)
			wiringdata.IOout(milModClass.pinData[0],0)
			
	elif mode == 1:
		for var in range(0,5):
			wiringdata.IOout(milModClass.pinData[0],1)
			wiringdata.IOout(milModClass.pinData[0],1)
			wiringdata.IOout(milModClass.pinData[0],0)
			wiringdata.IOout(milModClass.pinData[0],0)
	
	flg_Edge = 0
	data1 = -1
	
	for detectTime in range(0,250):
		data = wiringdata.IOin(milModClass.pinData[1])
		if (data == 1) and (flg_Edge == 0):# 1st Rising Edge
			flg_Edge = 1
			data1 = detectTime
			
		if (data == 0) and (flg_Edge == 1):# 1nd Falling Edge
			flg_Edge = 2
			
		if (data == 1) and (flg_Edge == 2):# 2nd Rising Edge
			print "detectTime = ",detectTime
			#340m/sec
			data1 = (340 * 100 * (data1 * 109.4 * 0.001 * 0.001))/2.0 # 1 : 200usec
			data2 = (340 * 100 * (detectTime * 109.4 * 0.001 * 0.001))/2.0 # 1 : 200usec
			return data1, data2
			
		time.sleep(0.00001) #0.01msec
	if data1 != -1:
		data1 = (340 * 100 * (data1 * 109.4 * 0.001 * 0.001))/2.0 # 1
		return data1,-1
	
	return data1,-1
	
def cleanup():
	AD2spibus.close()
