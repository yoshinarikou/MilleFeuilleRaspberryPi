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
modA = milMod.milMod(AD2ch.getInfo(0))	#connector number 0

if __name__=='__main__':
	try:

		while(1):
			modA.connect()
			returnData = AD2ch.read(modA,0)
			print "AD 0ch = ",returnData
			returnData = AD2ch.read(modA,1)
			print "AD 1ch = ",returnData
			modA.disconnect()
			time.sleep(1)



	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	AD2ch.cleanup()
	
