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
from milpy import DCMotor
import time

wiringdata.initIO()
mod0 = milMod.milMod(DCMotor.getInfo(0))	#Baseboard connector No.0
		
if __name__=='__main__':
	try:
		print "BD6211 voltage:3 ~ 7V   max current:1.0A."
		print "Do not add high voltage to motor. Examine the current, maximum 1.0A."
		while(1):
			mod0.connect()
			DCMotor.turnMotor(mod0, 1, 0)
			time.sleep(1)
			DCMotor.turnMotor(mod0, 1, 1)
			time.sleep(1)
			DCMotor.turnMotor(mod0, 0, 1)
			time.sleep(1)
			DCMotor.turnMotor(mod0, 1, 1)
			time.sleep(1)
			mod0.disconnect()
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	
