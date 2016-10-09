########################################################################
#	MCU Gear(R) system Sample Code
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	8/OCT/2016
#
#      ------ATTENTION------
#  "If you want to use this library, you need these command."
#  $sudo chmod 666 /sys/module/i2c_bcm2708/parameters/combined
#  $sudo echo -n 1 >  /sys/module/i2c_bcm2708/parameters/combined
#
########################################################################
#Revision Information
#
########################################################################
#!/usr/bin/python
from milpy import mil
from milpy import milMod
from milpy import wiringdata
from milpy import Accelerometer
import time

wiringdata.initIO()
modA = milMod.milMod(Accelerometer.getInfo(0))

if __name__=='__main__':
	try:
		print "If you want to use this library, you need these command before runninng."
		print "$sudo chmod 666 /sys/module/i2c_bcm2708/parameters/combined,"
		print "$sudo echo -n 1 >  /sys/module/i2c_bcm2708/parameters/combined."

		ID = Accelerometer.init()
		print"ID = ",ID
		
		#modA.connect() #I2C device do not need "connect()" and "disconnect()"
		
		while(1):
			accX = Accelerometer.get_X()
			print"X = ", accX
			accY = Accelerometer.get_Y()
			print"Y = ", accY
			accZ = Accelerometer.get_Z()
			print"Z = ", accZ
			
			time.sleep(1)
		
			print "while"

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	wiringdata.cleanup()
