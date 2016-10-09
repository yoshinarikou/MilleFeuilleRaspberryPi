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

#Please,set IOs 
#IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]
#in wiringdata.py

from milpy import mil
from milpy import milMod
from milpy import wiringdata
import time

#set up for GPIO device
wiringdata.initIO()
datas1 = [0x8000,0x0001]
datas1.extend(wiringdata.getWiring(0x80000001))
modA = milMod.milMod(datas1)

#digital out function
def myDout(milModClass, pinNo, HighLow):
	wiringdata.IOout(milModClass.pinData[pinNo],HighLow)

#digital in function
def myDin(milModClass, pinNo):
	return wiringdata.IOin(milModClass.pinData[pinNo])

if __name__=='__main__':
	try:
		print "Please,set IOs"
		print "IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]"
		print "in wiringdata.py"

		#HOLD test
		while(1):
			modA.connect()
			
			myDout(modA,0,1)
			myDout(modA,1,1)
			myDout(modA,2,1)
			myDout(modA,3,1)
			time.sleep(0.1)
			
			#close the gate and
			modA.HoldOn(0x0F) #hold all pins and dissconnect
			#modA.HoldOn(0x01) #hold pin 1 and dissconnect
			#modA.HoldOn(0x02) #hold pin 2 and dissconnect
			#modA.HoldOn(0x04) #hold pin 3 and dissconnect
			#modA.HoldOn(0x08) #hold pin 4 and dissconnect
			#modA.HoldOn(0x02 + 0x08) #hold pin 2, pin 4 and dissconnect
			
			print "Hold ON"
			
			#-------
			#These signal change is ignored.
			myDout(modA,0,0)
			myDout(modA,1,1)
			myDout(modA,2,0)
			myDout(modA,3,1)
			time.sleep(0.05)
			
			myDout(modA,0,1)
			myDout(modA,1,0)
			myDout(modA,2,1)
			myDout(modA,3,0)
			time.sleep(0.05)
			
			myDout(modA,0,0)
			myDout(modA,1,1)
			myDout(modA,2,0)
			myDout(modA,3,1)
			time.sleep(0.05)
			
			myDout(modA,0,1)
			myDout(modA,1,0)
			myDout(modA,2,1)
			myDout(modA,3,0)
			time.sleep(0.05)
			
			#-------
			
			#set initial output signal
			myDout(modA,0,0)
			myDout(modA,1,0)
			myDout(modA,2,0)
			myDout(modA,3,0)
			
			modA.connect() #connect before Hold off
			modA.HoldOff() #hold but not connect
			#time.sleep(0.01)
			print "Hold OFF"
			
			while(1):
				# stop process
				time.sleep(1)
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
