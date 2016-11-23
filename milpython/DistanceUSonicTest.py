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
from milpy import DistanceUSonic
import time

wiringdata.initIO()
mod0 = milMod.milMod(DistanceUSonic.getInfo(0))	#Baseboard connector No.0
		
if __name__=='__main__':
	try:
		mod0.connect()
		while(1):
			
			
			returnData = DistanceUSonic.read(mod0)
				
			print "Distance: ",returnData
			
			#mod0.disconnect()
			time.sleep(0.1)
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	
