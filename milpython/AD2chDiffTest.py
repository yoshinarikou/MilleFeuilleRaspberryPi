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
from milpy import AD2ch

import time

wiringdata.initIO()
modA = milMod.milMod(AD2ch.getInfo(0))	#Baseboard connector No.0

if __name__=='__main__':
	try:

		while(1):
			modA.connect()
			#The ch1 is referance voltage input pin.
			returnDataP = AD2ch.readSimpleDiff(modA)
			print "AD Diff = ",returnDataP
			print "Diff Voltage = ",returnDataP*(3.3/4095),"V"
			#A bit of data is 3.3V/4095bit = 0.0008058V/bit 
			
			modA.disconnect()
			time.sleep(1)



	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	AD2ch.cleanup()
	
