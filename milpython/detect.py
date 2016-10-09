########################################################################
#	MCU Gear(R) system detect devise
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
from milpy import wiringdata
from milpy import milMod
import time

#quick serch
#0x8*** ffff

try:
	#----------Serch setting---------------
	#serching range
	detectRangeTo = 0xfff
	#start address
	#default start address is 0x80000001
	addr1 = 0x8000
	addr2 = 0x0001
	#--------------------------------------
	
	mil.init()
	mil.detectInit()
	
	f = open('WiringInformation.txt', 'w')
	
	for var in range(0,detectRangeTo):
		
		addr0 = (addr1<< 16) + addr2
		#print "addr0 = ",hex(addr0)
		location = mil.detectModuleEx(addr1,addr2)
		
		if location != 0xff:
			print "location = ",location
			IOdata = wiringdata.getWiring(addr0)
			#save address
			#formattedmsg = "%d" % addr0
			d = f.write(str(addr0-0x80000000))
			#stringData = str(IOdata)
			d = f.write(str(IOdata))
			d = f.write("\r\n")
		
		#print "var =",var
		
		if addr2 == 0xffff:
			++addr1
			addr2 = 0x0000
			
		addr2 += 1
		
	f.close()
	
	mil.detectEnd()
	
	#print"location = ",location

	mil.cleanup()

	#sys.exit(location) #return value    
	#sys.exit([1,2,3,4]) #return value
except KeyboardInterrupt:
	print("detect key interrupt [ctrl]+ [C] \n")
	mil.cleanup()

