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
from milpy import mil
from milpy import milMod
from milpy import wiringdata
import time

wiringdata.initIO()

if __name__=='__main__':
	try:

		mil.restSignal()
		print "Reset Done"

			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
