##################################################################################################################
#	MCU Gear(R) system : mille-feuille Sample Code
#	GPIO Output test
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	06/Oct/2016
##################################################################################################################
#Revision Information
#
##################################################################################################################
#!/usr/bin/python

#Please,vset IOs 
#IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]
#in wiringdata.py

from mil import mil
from mil import milMod
from mil import p
from mil import wiringdata

import time

def myDout(milModClass, pinNo, HighLow):
	wiringdata.IOout(milModClass.pinData[pinNo],HighLow)

def myDin(milModClass, pinNo):
	wiringdata.IOin(milModClass.pinData[pinNo])

if __name__=='__main__':
	try:


		wiringdata.initIO()

		#GPIO
		datas1 = [0x8000,0x0001]
		datas1.extend(wiringdata.getWiring(0x80000001))
		print "datas1 = ",datas1
		modA = milMod.milMod(datas1)
		modA.connect()
		print "test 1"

		#HOLD test
		while(1):
			myDout(modA,0,1)
			myDout(modA,1,1)
			myDout(modA,2,1)
			myDout(modA,3,1)
			time.sleep(0.1)
			
			#If you close the gate, it 
			modA.HoldOn(0x0F) #hold all pins and dissconnect
			#modA.HoldOn(0x01) #hold pin 1 and dissconnect
			#modA.HoldOn(0x02) #hold pin 2 and dissconnect
			#modA.HoldOn(0x04) #hold pin 3 and dissconnect
			#modA.HoldOn(0x08) #hold pin 4 and dissconnect
			#modA.HoldOn(0x02 + 0x08) #hold pin 2, pin 4 and dissconnect
			
			#time.sleep(0.01)
			print "Hold ON"
			
			#-------
			#The signal change is ignored.
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
			
			myDout(modA,0,0)
			myDout(modA,1,0)
			myDout(modA,2,0)
			myDout(modA,3,0)
			
			modA.connect() #connect before Hold off
			modA.HoldOff() #hold but not connect
			#time.sleep(0.01)
			print "Hold OFF"
			while(1):
				time.sleep(1)
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
