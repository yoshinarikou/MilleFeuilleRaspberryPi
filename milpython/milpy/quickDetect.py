##################################################################################################################
#	MCU Gear(R) system : mille-feuille Sample Code
#	Quick detect function test
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

if __name__=='__main__':
	try:

		wiringdata.initIO()
		location = mil.quickDetectModule(0x4000,0x0005)
		print "quick detect location = ",location

			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
