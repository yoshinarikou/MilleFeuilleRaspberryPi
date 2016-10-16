########################################################################
#	MCU Gear(R) system wiringdata
#	Auther:y.kou.
#	web site: http://www.milletool.com/
#	Date	:	8/OCT/2016
#
########################################################################
#Revision Information
#
########################################################################
#!/usr/bin/python
import p
import mil
import RPi.GPIO as GPIO


def getWiring(myAddress):

	if myAddress == 0x80000001:
		#IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]] 
		IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]
	elif myAddress == 0x80000002:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]] 
		#IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]
	elif myAddress == 0x80000003:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]] 
		#IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]
	elif myAddress == 0x80000004:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]] 
		#IOdata = [p.inpin[0],p.inpin[1],p.inpin[2],p.inpin[3]]
	elif myAddress == 0x80000005:
		IOdata = [p.MOSI,p.MISO,p.SCLK,p.outpin[0]]
	elif myAddress == 0x80000006:
		IOdata = [p.MOSI,p.MISO,p.SCLK,p.outpin[0]]
	elif myAddress == 0x80000007:
		IOdata = [p.MOSI,p.MISO,p.SCLK,p.outpin[0]]
	elif myAddress == 0x80000008:
		IOdata = [p.MOSI,p.MISO,p.SCLK,p.outpin[0]]
	elif myAddress == 0x80000009:
		IOdata = [p.MOSI,p.outpin[0],p.SCLK,p.outpin[1]]
	elif myAddress == 0x8000000A:
		IOdata = [p.MOSI,p.outpin[0],p.SCLK,p.outpin[1]]
	elif myAddress == 0x8000000B:
		IOdata = [p.MOSI,p.outpin[0],p.SCLK,p.outpin[1]]
	elif myAddress == 0x8000000C:
		IOdata = [p.MOSI,p.outpin[0],p.SCLK,p.outpin[1]]
	elif myAddress == 0x8000000D:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x8000000E:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x8000000F:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x80000010:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x80000015:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000016:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000017:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000018:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000019:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC]
	elif myAddress == 0x8000001A:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
	elif myAddress == 0x8000001B:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
	elif myAddress == 0x8000001C:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
	elif myAddress == 0x8000001D:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]] 
	elif myAddress == 0x8000001E:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]
	elif myAddress == 0x8000001F:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]
	elif myAddress == 0x80000020:
		IOdata = [p.outpin[0],p.outpin[1],p.outpin[2],p.outpin[3]]
	elif myAddress == 0x80000021:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000022:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000023:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000024:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000025:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000026:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000027:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000028:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000029:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
	elif myAddress == 0x8000002A:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
	elif myAddress == 0x8000002B:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
	elif myAddress == 0x8000002C:
		IOdata = [p.outpin[0],p.inpin[0],p.NC,p.NC] 
		
	elif myAddress == 0x8000002D:
		IOdata = [p.outpin[0],p.outpin[1]]
	elif myAddress == 0x8000002E:
		IOdata = [p.outpin[0],p.outpin[1]]
	elif myAddress == 0x8000002F:
		IOdata = [p.outpin[0],p.outpin[1]]
	elif myAddress == 0x80000030:
		IOdata = [p.outpin[0],p.outpin[1]]
	elif myAddress == 0x80000031:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x80000032:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x80000033:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
	elif myAddress == 0x80000034:
		IOdata = [p.outpin[0],p.MISO,p.SCLK]
		
	elif myAddress == 0x80000039:
		IOdata = [p.outpin[0],p.NC,p.NC,p.NC]
	elif myAddress == 0x8000003A:
		IOdata = [p.outpin[0],p.NC,p.NC,p.NC]
	elif myAddress == 0x8000003B:
		IOdata = [p.outpin[0],p.NC,p.NC,p.NC]
	elif myAddress == 0x8000003C:
		IOdata = [p.outpin[0],p.NC,p.NC,p.NC]
		
	elif myAddress == 0x8000003D:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x8000003E:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x8000003F:
		IOdata = [p.SDA,p.SCL]
	elif myAddress == 0x80000040:
		IOdata = [p.SDA,p.SCL]
		
	elif myAddress == 0xc0000001:
		IOdata = [p.outpin[0],p.outpin[1], p.Rx, p.Tx]

	return IOdata

def initIO():

	GPIO.setmode(GPIO.BCM)

	for var in range(0,len(p.inpin)):
		GPIO.setup(p.inpin[var], GPIO.IN) #set inpin as a input
			
	for var in range(0,len(p.outpin)):
		GPIO.setup(p.outpin[var], GPIO.OUT) #set outpin as a output
		
def IOout(IoNo,out):
	GPIO.output(IoNo,out)
	
def IOin(IoNo):
	return GPIO.input(IoNo)

def cleanup():
	GPIO.cleanup()
	
def checkSetting():
	return 0
