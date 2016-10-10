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
from milpy import Proximity
import time

wiringdata.initIO()
mod0 = milMod.milMod(Proximity.getInfo(0))
		
if __name__=='__main__':
	try:
		print "Check with white paper. Detecting distance is under 5mm."
		while(1):
			mod0.connect()
			Proximity.power(mod0,1)#power ON
			readData = Proximity.read(mod0)
			Proximity.power(mod0,0)#power OFF
			print "read data = ",readData
			time.sleep(0.1)
			mod0.disconnect()
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	
