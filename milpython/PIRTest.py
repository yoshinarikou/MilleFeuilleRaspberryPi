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
from milpy import PIR
import time

wiringdata.initIO()
mod0 = milMod.milMod(PIR.getInfo(0))	#Baseboard connector No.0
		
if __name__=='__main__':
	try:
		
		
		
		while(1):
			mod0.connect()
			
			readData = PIR.read(mod0)
			
			print "read data = ",readData
			
			mod0.disconnect()
			
			time.sleep(0.1)
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	
