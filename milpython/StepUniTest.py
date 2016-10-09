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
from milpy import StepUni
import time

wiringdata.initIO()
mod0 = milMod.milMod(StepUni.getInfo(0))
mod1 = milMod.milMod(StepUni.getInfo(1))
#print StepUni.getInfo(0)
		
if __name__=='__main__':
	try:
		
		while(1):
			print"try connect"
			mod0.connect()
			StepUni.stopStep(mod0)
			print "try move"
			StepUni.moveStep(mod0,True, 100,0.003)	# 10 steps, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.moveStep(mod0,False, 100,0.003)	# 10 steps, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.stopStep(mod0)
			mod0.disconnect()
			
			time.sleep(1)
			
			mod1.connect()
			StepUni.stopStep(mod1)
			print "try move"
			StepUni.moveStep(mod1,True, 100,0.003)	# 10 steps, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.moveStep(mod1,False, 100,0.003)	# 10 steps, delay time 0.001sec (We tested chinese stepping motor ST-42BYG0506H) 
			StepUni.stopStep(mod1)
			mod1.disconnect()
			time.sleep(3)
			

	except KeyboardInterrupt:
		print("detect key interrupt [ctrl]+ [C] \n")

	mil.cleanup()
	wiringdata.cleanup()
	
