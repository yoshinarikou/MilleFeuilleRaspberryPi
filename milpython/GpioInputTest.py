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

from milpy import gpio

import time

#set up for GPIO device
wiringdata.initIO()
modA = milMod.milMod(gpio.getInfo(0))	#Baseboard connector No.0


if __name__=='__main__':
	try:
		
		print "Please,set IOs"
		print "IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]"
		print "in wiringdata.py"
		
		while(1):
			modA.connect()	
			print " "
			print "myPin 1 = ",gpio.DigitalIn(modA,0)
			print "myPin 2 = ",gpio.DigitalIn(modA,1)
			print "myPin 3 = ",gpio.DigitalIn(modA,2)
			print "myPin 4 = ",gpio.DigitalIn(modA,3)
			time.sleep(1)
			modA.disconnect()	


	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
