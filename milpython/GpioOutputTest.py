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

from milpy import gpio

import time

#set up for GPIO device
wiringdata.initIO()
modA = milMod.milMod(gpio.getInfo(0))	#Baseboard connector No.0


if __name__=='__main__':
	try:
		print "Please,set IOs"
		print "IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]"
		print "in wiringdata.py"
		
		#GPIO OUT test
		while(1):
			modA.connect()
			gpio.DigitalOut(modA, 0, 1)
			gpio.DigitalOut(modA, 1, 0)
			gpio.DigitalOut(modA, 2, 0)
			gpio.DigitalOut(modA, 3, 0)
			time.sleep(0.1)
			
			gpio.DigitalOut(modA, 0, 0)
			gpio.DigitalOut(modA, 1, 1)
			gpio.DigitalOut(modA, 2, 0)
			gpio.DigitalOut(modA, 3, 0)
			time.sleep(0.1)
			
			gpio.DigitalOut(modA, 0, 0)
			gpio.DigitalOut(modA, 1, 0)
			gpio.DigitalOut(modA, 2, 1)
			gpio.DigitalOut(modA, 3, 0)
			time.sleep(0.1)
			
			gpio.DigitalOut(modA, 0, 0)
			gpio.DigitalOut(modA, 1, 0)
			gpio.DigitalOut(modA, 2, 0)
			gpio.DigitalOut(modA, 3, 1)
			time.sleep(0.1)
			
			modA.disconnect()
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
