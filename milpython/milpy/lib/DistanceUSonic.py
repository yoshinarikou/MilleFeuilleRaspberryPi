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
import time

moduleAddress1 = 0x8000
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

	return moduleAddress1,moduleAddress2

def getIOs():
	IOdata = wiringdata.getWiring(moduleAddress)
	return IOdata
	
def power(milModClass, OnOff):
	wiringdata.IOout(milModClass.pinData[0],OnOff)

def read(milModClass):
	wiringdata.IOout(milModClass.pinData[0],1)
	time.sleep(0.0001)#send ultrasonic
	wiringdata.IOout(milModClass.pinData[0],0)

	flg_Edge = 0
	data1 = -1
	rData1 = -1
	
	for detectTime in range(0,500):
		data = wiringdata.IOin(milModClass.pinData[1])
		if (data == 1) and (flg_Edge == 0):# 1st Rising Edge
			flg_Edge = 1
			data1 = detectTime
			
		if (data == 0) and (flg_Edge == 1):# 1nd Falling Edge
			flg_Edge = 2
			
		if (data == 1) and (flg_Edge == 2):# 2nd Rising Edge
			#print "detectTime = ",detectTime
			#340.29m/sec
			rData1 = (data1 * 109.4 * 0.001 * 0.001)*100/2.0
			rData2 = (detectTime * 109.4 * 0.001 * 0.001)*100/2.0
			data1 = (340.29 * 100 * (data1 * 109.4 * 0.001 * 0.001))/2.0 # 1 : 200usec
			data2 = (340.29 * 100 * (detectTime * 109.4 * 0.001 * 0.001))/2.0 # 1 : 200usec
			return rData1,rData2, data1, data2
			
		time.sleep(0.00001) #0.01msec
	if data1 != -1:
		rData1 = (data1 * 109.4 * 0.001 * 0.001)*100/2.0
		data1 = (340.29 * 100 * (data1 * 109.4 * 0.001 * 0.001))/2.0 # 1
		return rData1,-1, data1,-1
	
	return data1,-1
	

def holdConnect(milModClass):
	milModClass.connect() #connect before Hold off
	milModClass.HoldOff() #hold but not connect

def holdDisconnect(milModClass):
	milModClass.HoldOn(0x01)
