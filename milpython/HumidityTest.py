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
from milpy import Humidity
import time

wiringdata.initIO()
modA = milMod.milMod(Humidity.getInfo(0))
		
if __name__=='__main__':
	try:
		Humidity.init()

		#modA.connect()#I2C devices not need connect command
		
		while(1):
			Temp = Humidity.readTemp()
			print "Temparature = " , Temp[0] , "raw Data = ", hex(Temp[1])
			Humid = Humidity.readHumidity()
			print "Humidity = " , Humid[0] , "raw Data = ", hex(Humid[1])
			time.sleep(1)

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
