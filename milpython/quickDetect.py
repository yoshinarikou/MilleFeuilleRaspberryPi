########################################################################
#	MCU Gear(R) system detect devise
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	8/OCT/2016
#
#	This detect is that can find devices over the number of address 
########################################################################
#Revision Information
#
########################################################################
#!/usr/bin/python

from milpy import mil
from milpy import milMod
from milpy import wiringdata
import time

if __name__=='__main__':
	try:

		wiringdata.initIO()
		location = mil.quickDetectModule(0x4000,0x0001) #address 0x8000 0001
		print "quick detect location = ",location

			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
