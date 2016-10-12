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
from milpy import AirPressure
from milpy import Humidity
from milpy import LightSensor
from milpy import Pwm
from milpy import StepUni
import time
import os
os.popen("sudo chmod 666 /sys/module/i2c_bcm2708/parameters/combined",'w').write("kikaika")
os.popen("sudo echo -n 1 >  /sys/module/i2c_bcm2708/parameters/combined",'w').write("kikaika")

wiringdata.initIO()
modA = milMod.milMod(Accelerometer.getInfo(0))
modB = milMod.milMod(AirPressure.getInfo(3))
modC = milMod.milMod(Humidity.getInfo(1))
modD = milMod.milMod(LightSensor.getInfo(2))
modA = milMod.milMod(Pwm.getInfo(1))

mod0 = milMod.milMod(StepUni.getInfo(0))
mod1 = milMod.milMod(StepUni.getInfo(1))
		

if __name__=='__main__':
	try:
		print "If you want to use this library, you need these command before runninng."
		print "$sudo chmod 666 /sys/module/i2c_bcm2708/parameters/combined,"
		print "$sudo echo -n 1 >  /sys/module/i2c_bcm2708/parameters/combined."

		ID = Accelerometer.init()
		print"ID = ",ID
		
		Humidity.init()
		
		#modA.connect() #I2C device do not need "connect()" and "disconnect()"
		
		while(1):
			#-----
			accX = Accelerometer.get_X()
			print"X = ", accX
			accY = Accelerometer.get_Y()
			print"Y = ", accY
			accZ = Accelerometer.get_Z()
			print"Z = ", accZ
			#-----
			data = AirPressure.getCalibData()
			TAndP = AirPressure.read(data)
			print"T = ",TAndP[0],"deg"
			print"P = ",TAndP[1],"hPa"
			print"Altitude = ",TAndP[2],"m"
			#-----
			Temp = Humidity.readTemp()
			print "Temparature = " , Temp[0] , "raw Data = ", hex(Temp[1])
			Humid = Humidity.readHumidity()
			print "Humidity = " , Humid[0] , "raw Data = ", hex(Humid[1])
			time.sleep(1)
			#-----
			
			modD.connect()
			readData = LightSensor.Read(modD)
			print "readData = ",readData
			modD.disconnect()

			#-----
			Pwm.setServoPulse(0,308)
			Pwm.setServoPulse(1,495)
			Pwm.time.sleep(1)
			Pwm.setServoPulse(1,308)
			Pwm.setServoPulse(0,495)
			time.sleep(1)
			#----
			
			print"try connect"
			mod0.connect()
			StepUni.stopStep(mod0)
			print "try move"
			StepUni.moveStep(mod0,True, 30,0.003)	# 30 cycle, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.moveStep(mod0,False, 30,0.003)	# 30 cycle, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.stopStep(mod0)
			mod0.disconnect()
			
			
			mod1.connect()
			StepUni.stopStep(mod1)
			print "try move"
			StepUni.moveStep(mod1,True, 30,0.003)	# 30 cycle, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.moveStep(mod1,False, 30,0.003)	# 30 cycle, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.stopStep(mod1)
			mod1.disconnect()
			
			#second connect function test-----
			print "second connect test."
			mod0.connect()
			mod1.secondConnect()
			for var in range(0,100):
				StepUni.movTwinOneStep(mod0, [1,0,0,0], mod1, [1,0,0,0])
				time.sleep(0.004)
				StepUni.movTwinOneStep(mod0, [1,1,0,0], mod1, [1,1,0,0])
				time.sleep(0.002)
				
				StepUni.movTwinOneStep(mod0, [0,1,0,0], mod1, [0,1,0,0])
				time.sleep(0.004)
				StepUni.movTwinOneStep(mod0, [0,1,1,0], mod1, [0,1,1,0])
				time.sleep(0.002)
				
				StepUni.movTwinOneStep(mod0, [0,0,1,0], mod1, [0,0,1,0])
				time.sleep(0.004)
				StepUni.movTwinOneStep(mod0, [0,0,1,1], mod1, [0,0,1,1])
				time.sleep(0.002)
				
				StepUni.movTwinOneStep(mod0, [0,0,0,1], mod1, [0,0,0,1])
				time.sleep(0.004)
				StepUni.movTwinOneStep(mod0, [1,0,0,1], mod1, [1,0,0,1])
				time.sleep(0.002)
				
			mod0.disconnect()
			mod1.disconnect()
			#-----
			
			print "while"

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	wiringdata.cleanup()
