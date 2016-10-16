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
from milpy import DA1ch
import time

wiringdata.initIO()
modA = milMod.milMod(DA1ch.getInfo(0))	#Baseboard connector No.0

if __name__=='__main__':
	try:
		while(1):
			modA.connect()
			returnData = DA1ch.write(modA,0xfff)	#MAX Voltaga
			print "DA = 0xfff"
			time.sleep(1)
			returnData = DA1ch.write(modA,0x000)	#MIN Voltaga
			print "DA = 0x000"
			modA.disconnect()
			time.sleep(1)

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	DA1ch.cleanup()
	
