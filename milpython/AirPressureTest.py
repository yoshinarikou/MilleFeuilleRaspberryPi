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
from milpy import AirPressure
import time

wiringdata.initIO()
modA = milMod.milMod(AirPressure.getInfo(0))

if __name__=='__main__':
	try:
		#modA.connect() #I2C device do not need "connect()" and "disconnect()"
		
		while(1):			
			data = AirPressure.getCalibData()
			TAndP = AirPressure.read(data)
			print"T = ",TAndP[0],"deg"
			print"P = ",TAndP[1],"hPa"
			print"Altitude = ",TAndP[2],"m"
			time.sleep(1)
			
	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
