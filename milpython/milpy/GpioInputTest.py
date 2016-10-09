##################################################################################################################
#	MCU Gear(R) system : mille-feuille Sample Code
#
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	06/Oct/2016
##################################################################################################################
#Revision Information
#
##################################################################################################################
#!/usr/bin/python

#set IOs 
#IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]
#in wiringdata.py

from mil import mil
from mil import milMod
from mil import p
from mil import wiringdata

import time

def myDout(milModClass, pinNo, HighLow):
	wiringdata.IOout(milModClass.pinData[pinNo],HighLow)

def myDin(milModClass, pinNo):
	return wiringdata.IOin(milModClass.pinData[pinNo])

if __name__=='__main__':
	try:
		wiringdata.initIO()

		#GPIO
		datas1 = [0x8000,0x0001]
		datas1.extend(wiringdata.getWiring(0x80000001))
		modA = milMod.milMod(datas1)
		modA.connect()
		
		print "test 1"
		
		while(1):
			
			print " "
			print "myPin 1 = ",myDin(modA,0)
			print "myPin 2 = ",myDin(modA,1)
			print "myPin 3 = ",myDin(modA,2)
			print "myPin 4 = ",myDin(modA,3)
			time.sleep(1)


	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
