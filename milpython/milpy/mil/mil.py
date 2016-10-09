#!/usr/bin/python

import RPi.GPIO as GPIO
import spidev
import p
import time
import wiringdata

spi=spidev.SpiDev()
spi.open(0,0)

BaseSPIdelay = 0.000001
#BaseSPIdelay = 0.001
#BaseSPIdelay = 0.3
BaseSPIHz = 17000000
#BaseSPIHz = 15000000
ModuleSPIdelay = 0.000001
#ModuleSPIdelay = 0.001
#ModuleSPIdelay = 0.3
ModuleSPIHz = 17000000
#ModuleSPIHz = 15000000

#spibus = spidev.SpiDev(0,0)
#spibus.max_speed_hz = 20000000

#BaseSPIHz= 15000000
#ModSPIHz = 15000000
#ModWriteSPIHz = 15000000

#BaseSPIHz= 1000000
#ModSPIHz = 1000000
#ModWriteSPIHz = 1000000

def setmode():
	GPIO.setmode(GPIO.BCM)

#def setup(pinNo, Dir):
#	if Dir == False:
#		GPIO.setup(pinNo, GPIO.IN)
#	elif Dir == True:
#		GPIO.setup(pinNo, GPIO.OUT)
		
def cleanup():
	GPIO.cleanup()
	spi.close()

def init():
	GPIO.setmode(GPIO.BCM)

	for var in range(0,len(p.inpin)-1):
		GPIO.setup(p.inpin[var], GPIO.IN) #set inpin as a input
		
	for var in range(0,len(p.outpin)-1):
		GPIO.setup(p.outpin[var], GPIO.OUT) #set outpin as a output
		
	

#def initBase():
	#send reset signal

#def connectPin(location, pinData):
		
def HoldOn(address1,address2):
	writeModule(address1,address2,0x0B,0xFF)
	
def HoldOff(address1,address2):
	writeModule(address1,address2,0x0C,0xFF)
	

#def module_boards_all_off():
	
#def disconnectPin(BANK):


def writeBase(data1,data2):
	spi.mode = 0
	#print "writeBase data1 = ",data1,"data2 = ",data2
	#spi.max_speed_hz = 1000000
	spi.max_speed_hz = BaseSPIHz
	resp=spi.xfer2([0x80])
	resp=spi.xfer2([0x00])
	resp=spi.xfer2([0x00])
	resp=spi.xfer2([0x00])
	resp=spi.xfer2([data1])
	resp=spi.xfer2([data2])
	time.sleep(BaseSPIdelay)


def getUartAddr():
	spi.mode = 0
	#spi.max_speed_hz = 1000000
	spi.max_speed_hz = BaseSPIHz
	resp=spi.xfer2([0x80])
	resp=spi.xfer2([0x00])
	resp=spi.xfer2([0x00])
	resp=spi.xfer2([0x00])
	resp=spi.xfer2([0xee])
	resp=spi.xfer2([0xee])
	time.sleep(BaseSPIdelay)
	time.sleep(0.1)
	resp=spi.xfer2([0x80])
	time.sleep(0.1)
	#print "-------"
	#print "resp = ",resp
	resp=spi.xfer2([0x00])
	#print "resp = ",resp
	resp=spi.xfer2([0x00])
	#print "resp = ",resp
	resp=spi.xfer2([0x00])
	#print "resp = ",resp
	resp=spi.xfer2([0x00])
	#print "resp = ",resp
	resp=spi.xfer2([0x00])
	#print "resp = ",resp
	#print "-------"
	time.sleep(BaseSPIdelay)

	


def writeModule(address1,address2,data1,data2):
	spi.mode = 0
	#print "writeModule data1 = ",data1,"data2 = ",data2
	
	#spi.max_speed_hz = 1000000
	spi.max_speed_hz = ModuleSPIHz
	addr1=(address1>>8) & 0x00ff
	addr2=(address1 & 0x00ff)
	addr3=(address2>>8) & 0x00ff
	addr4=(address2 & 0x00ff)

	resp=spi.xfer2([addr1])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([addr2])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([addr3])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([addr4])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([data1])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([data2])
	time.sleep(ModuleSPIdelay)
	
def restSignal():
	spi.mode = 0
	
	#spi.max_speed_hz = 1000000
	spi.max_speed_hz = ModuleSPIHz

	resp=spi.xfer2([0x00])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([0x00])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([0x00])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([0x00])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([0x00])
	#time.sleep(ModuleSPIdelay)

	resp=spi.xfer2([0x00])
	time.sleep(ModuleSPIdelay)
	

def changeBank(bank):
	#writeBase(0x70,bank)
	print "change bank = ",bank

def openModule(address1,address2,pinType):
	#writeModule((address>>8),(address & 0x00ff),0x02,0xff)
	#writeModule(address1,address2,0x02,0xff)
	writeModule(address1,address2,pinType,0xff)
	#print "open addr1 = ",hex(address1)," open addr2 = ",hex(address2),"pintype = ",hex(pinType)

def closeModule(address1,address2):
	#writeModule((address>>8),(address & 0x00ff),0x01,0xff)
	writeModule(address1,address2,0x01,0xff)

def detectInit():
	writeBase(1,0x11)
	writeBase(5,0x12)
	writeBase(9,0x13)
	writeBase(13,0x14)

	#writeBase(1,0x15)
	#writeBase(5,0x16)
	#writeBase(9,0x17)
	#writeBase(13,0x18)
	
def detectEnd():
	#writeBase(1,0xff)
	#writeBase(5,0xff)
	#writeBase(9,0xff)
	#writeBase(13,0xff)
	
	writeBase(1,0x00)
	writeBase(5,0x00)
	writeBase(9,0x00)
	writeBase(13,0x00)
	
	

def IO(IoNo,out):
	GPIO.output(IoNo,out)
	
def IOin(IoNo):
	return GPIO.input(IoNo)

def detectModule(address1,address2):

	#print "address1 = ",hex(address1)," address2 = ",hex(address2)
	detectInit()
	location = 0xff

	#writeModule((address>>8),(address & 0x00ff),0x03,0xff)
	#time.sleep(0.1)
	writeModule(address1,address2,0x03,0xff)
	#time.sleep(5)

	#if GPIO.input(p.inpin[4])==False:
	if wiringdata.IOin(p.inpin[0])==False:
		#print("CON 1")
		location = 1
	#elif GPIO.input(p.inpin[5])==False:
	elif wiringdata.IOin(p.inpin[1])==False:
		#print("CON 2")
		location = 5
	#elif GPIO.input(p.inpin[6])==False:
	elif wiringdata.IOin(p.inpin[2])==False:
		#print("CON 3")
		location = 9
	#elif GPIO.input(p.inpin[7])==False:
	elif wiringdata.IOin(p.inpin[3])==False:
		#print("CON 4")
		location = 13
	
	#writeModule((address>>8),(address & 0x00ff),0x04,0xff)
	writeModule(address1,address2,0x04,0xff)

	detectEnd()

	return location



def detectModuleEx(address1,address2):

	#print "address1 = ",hex(address1)," address2 = ",hex(address2)
	#detectInit()
	location = 0xff

	#writeModule((address>>8),(address & 0x00ff),0x03,0xff)
	#time.sleep(0.1)
	writeModule(address1,address2,0x03,0xff)
	#time.sleep(5)

	#if GPIO.input(p.inpin[4])==False:
	if wiringdata.IOin(p.inpin[0])==False:
		#print("CON 1")
		location = 1
	#elif GPIO.input(p.inpin[5])==False:
	elif wiringdata.IOin(p.inpin[1])==False:
		#print("CON 2")
		location = 5
	#elif GPIO.input(p.inpin[6])==False:
	elif wiringdata.IOin(p.inpin[2])==False:
		#print("CON 3")
		location = 9
	#elif GPIO.input(p.inpin[7])==False:
	elif wiringdata.IOin(p.inpin[3])==False:
		#print("CON 4")
		location = 13
	
	#writeModule((address>>8),(address & 0x00ff),0x04,0xff)
	writeModule(address1,address2,0x04,0xff)

	#detectEnd()

	return location


def quickDetectModule(address1,address2):

	#print "address1 = ",hex(address1)," address2 = ",hex(address2)
	detectInit()
	location = 0xff

	#writeModule((address>>8),(address & 0x00ff),0x03,0xff)
	#time.sleep(0.1)
	writeModule(address1,address2,0x03,0xff)
	#time.sleep(5)

	#if GPIO.input(p.inpin[4])==False:
	if wiringdata.IOin(p.inpin[0])==False:
		#print("CON 1")
		location = 1
	#elif GPIO.input(p.inpin[5])==False:
	elif wiringdata.IOin(p.inpin[1])==False:
		#print("CON 2")
		location = 5
	#elif GPIO.input(p.inpin[6])==False:
	elif wiringdata.IOin(p.inpin[2])==False:
		#print("CON 3")
		location = 9
	#elif GPIO.input(p.inpin[7])==False:
	elif wiringdata.IOin(p.inpin[3])==False:
		#print("CON 4")
		location = 13
	
	#writeModule((address>>8),(address & 0x00ff),0x04,0xff)
	writeModule(address1,address2,0x04,0xff)

	detectEnd()

	return location



def testModule(address1,address2):
	
	#data1
	#0x01 close all gate
	#0x02 open 4 normal IOs
	#0x03 Detect mode ON
	#0x04 Detect mode OFF
	#0x05 LED on
	#0x06 LED off
	#0x07 MOSI MIDO SCK 4
	#0x08 MOSI 2 SCK 4
	#0x09 1 2 SCK 4
	#0x0A 1 MISO SCK 4
	
	
	#writeModule(0x0000,0x0000,0x00,0x00)
	writeModule(address1,address2,0x03,0xff)
	while(1):
		time.sleep(0.01)
	writeModule(address1,address2,0x09,0xff)
	time.sleep(0.01)
	while(1):
		writeModule(0xAAAA,address2,0x03,0xff)
		time.sleep(0.1)
		

