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
moduleAddress2 = 0x001D
moduleAddress = 0x8000001D

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
	
def stopStep(milModClass):
	wiringdata.IOout(milModClass.pinData[0],0)#Y2
	wiringdata.IOout(milModClass.pinData[1],0)#Y1
	wiringdata.IOout(milModClass.pinData[2],0)#X2
	wiringdata.IOout(milModClass.pinData[3],0)#X1

def movOneStep(milModClass, pinHighLow):
	wiringdata.IOout(milModClass.pinData[3],pinHighLow[0])#X1
	wiringdata.IOout(milModClass.pinData[1],pinHighLow[1])#Y1
	wiringdata.IOout(milModClass.pinData[2],pinHighLow[2])#X2
	wiringdata.IOout(milModClass.pinData[0],pinHighLow[3])#Y2
	

def moveStep(milModClass,Direction, StepNum,DELAY1):
	#DELAY1 = 0.001 max speed
	DELAY2 = DELAY1*2
	
	if Direction == True:
		for var in range(0,StepNum):
			
			print "var = ",var
			
			wiringdata.IOout(milModClass.pinData[3],1)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],1)#X1
			wiringdata.IOout(milModClass.pinData[1],1)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],1)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],1)#Y1
			wiringdata.IOout(milModClass.pinData[2],1)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],1)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],1)#X2
			wiringdata.IOout(milModClass.pinData[0],1)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],1)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],1)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],1)#Y2
			time.sleep(DELAY1)
	
	else:
		for var in range(0,StepNum):
			
			print "var = ",var
			
			wiringdata.IOout(milModClass.pinData[3],1)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],1)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],1)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],1)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],1)#X2
			wiringdata.IOout(milModClass.pinData[0],1)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],0)#Y1
			wiringdata.IOout(milModClass.pinData[2],1)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],1)#Y1
			wiringdata.IOout(milModClass.pinData[2],1)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.pinData[3],0)#X1
			wiringdata.IOout(milModClass.pinData[1],1)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.pinData[3],1)#X1
			wiringdata.IOout(milModClass.pinData[1],1)#Y1
			wiringdata.IOout(milModClass.pinData[2],0)#X2
			wiringdata.IOout(milModClass.pinData[0],0)#Y2
			time.sleep(DELAY1)




def movTwinOneStep(milModClass1, pinHighLow1, milModClass2, pinHighLow2):
	wiringdata.IOout(milModClass1.pinData[3],pinHighLow1[0])#X1
	wiringdata.IOout(milModClass1.pinData[1],pinHighLow1[1])#Y1
	wiringdata.IOout(milModClass1.pinData[2],pinHighLow1[2])#X2
	wiringdata.IOout(milModClass1.pinData[0],pinHighLow1[3])#Y2
	
	wiringdata.IOout(milModClass2.secondPinData[3],pinHighLow2[0])#X1
	wiringdata.IOout(milModClass2.secondPinData[1],pinHighLow2[1])#Y1
	wiringdata.IOout(milModClass2.secondPinData[2],pinHighLow2[2])#X2
	wiringdata.IOout(milModClass2.secondPinData[0],pinHighLow2[3])#Y2
	
	
def moveSecondStep(milModClass,Direction, StepNum,DELAY1):
	#DELAY1 = 0.001 max speed
	DELAY2 = DELAY1*2
	
	if Direction == True:
		for var in range(0,StepNum):
			
			print "var = ",var
			print "milModClass.secondPinData[3] = ",milModClass.secondPinData[3]
			wiringdata.IOout(milModClass.secondPinData[3],1)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],1)#X1
			wiringdata.IOout(milModClass.secondPinData[1],1)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],1)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],1)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],1)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],1)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],1)#X2
			wiringdata.IOout(milModClass.secondPinData[0],1)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],1)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],1)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],1)#Y2
			time.sleep(DELAY1)
	
	else:
		for var in range(0,StepNum):
			
			print "var = ",var
			
			wiringdata.IOout(milModClass.secondPinData[3],1)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],1)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],1)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],1)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],1)#X2
			wiringdata.IOout(milModClass.secondPinData[0],1)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],0)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],1)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],1)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],1)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY1)
			
			wiringdata.IOout(milModClass.secondPinData[3],0)#X1
			wiringdata.IOout(milModClass.secondPinData[1],1)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY2)
			
			wiringdata.IOout(milModClass.secondPinData[3],1)#X1
			wiringdata.IOout(milModClass.secondPinData[1],1)#Y1
			wiringdata.IOout(milModClass.secondPinData[2],0)#X2
			wiringdata.IOout(milModClass.secondPinData[0],0)#Y2
			time.sleep(DELAY1)
