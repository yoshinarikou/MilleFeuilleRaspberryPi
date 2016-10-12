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
from milpy import Pwm
import time

wiringdata.initIO()
modA = milMod.milMod(Pwm.getInfo(0))

if __name__=='__main__':
	try:
	
		Pwm.initPwm()

		#modA.connect()#I2C devices not need connect command

		while(1):
			Pwm.setServoPulse(0,308)
			Pwm.setServoPulse(1,495)
			Pwm.time.sleep(1)
			Pwm.setServoPulse(1,308)
			Pwm.setServoPulse(0,495)
			time.sleep(1)
	

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
