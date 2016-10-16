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
from milpy import Relay
import time

wiringdata.initIO()
mod0 = milMod.milMod(Relay.getInfo(0))	#Baseboard connector No.0
		
if __name__=='__main__':
	try:
		while(1):
			#mod0.connect()
			Relay.holdConnect(mod0)  # We highly recomend to use this function for relay.
			time.sleep(2)
			print "power ON"
			Relay.power(mod0, 1)
			time.sleep(2)
			#mod0.disconnect()
			Relay.holdDisconnect(mod0)  # We highly recomend to use this function for relay.
			time.sleep(2)
			
			
			#mod0.connect()
			Relay.holdConnect(mod0)  # We highly recomend to use this function for relay.
			time.sleep(2)
			print "power OFF"
			Relay.power(mod0, 0)
			time.sleep(2)
			#mod0.disconnect()
			Relay.holdDisconnect(mod0)  # We highly recomend to use this function for relay.
			time.sleep(2)
			
			
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	
