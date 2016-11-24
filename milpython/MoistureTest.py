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
from milpy import Moisuture
import time

wiringdata.initIO()
modA = milMod.milMod(Moisuture.getInfo(0))
		
if __name__=='__main__':
	try:
		modA.connect()
		
		while(1):
			modA.connect()
			readData = Moisuture.read(modA)
			print "readData = ",readData
			time.sleep(1)
			modA.disconnect()

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	wiringdata.cleanup()
