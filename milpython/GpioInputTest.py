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

#set IOs 
#IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]
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
		print "IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]"
		print "in wiringdata.py"
		
		while(1):
			modA.connect()	
			print " "
			print "myPin 1 = ",myDin(modA,0)
			print "myPin 2 = ",myDin(modA,1)
			print "myPin 3 = ",myDin(modA,2)
			print "myPin 4 = ",myDin(modA,3)
			time.sleep(1)
			modA.disconnect()	


	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
