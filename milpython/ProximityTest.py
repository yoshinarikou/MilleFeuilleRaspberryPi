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
mod0 = milMod.milMod(Proximity.getInfo(0))	#Baseboard connector No.0
		
if __name__=='__main__':
	try:
		
		print "Check with white paper. Detecting distance is under 5mm."
		
		#initiarize power ON. You can control LED power of proximity sensor.
		Proximity.holdConnect(mod0)  # We highly recomend to use this function for Proximity.
		Proximity.power(mod0,1)#power ON
		time.sleep(0.5)#worm up
		Proximity.holdDisconnect(mod0)  # We highly recomend to use this function for Proximity.
		
		
		while(1):
			#mod0.connect()
			Proximity.holdConnect(mod0)  # We highly recomend to use this function for Proximity.
			
			#Proximity.power(mod0,1)#power ON
			#time.sleep(0.5)#worm up
			
			readData = Proximity.read(mod0)
			
			#Proximity.power(mod0,0)#power OFF
			
			print "read data = ",readData
			
			#mod0.disconnect()
			Proximity.holdDisconnect(mod0)  # We highly recomend to use this function for Proximity.
			
			time.sleep(0.1)
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	
