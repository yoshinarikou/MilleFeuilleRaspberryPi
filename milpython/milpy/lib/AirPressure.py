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
from ..mil import mil
#import smbus
from ..mil import p
from ..mil import wiringdata
import time
import struct, array, time, io, fcntl

I2C_address = 0x76
TEMP = 0x00
HUMIDITY = 0x01
CONF = 0x02
MANUID= 0xFE
DEVICEID= 0xFF

moduleAddress1 = 0x8000
moduleAddress2 = 0x0025
moduleAddress = 0x80000025


I2C_SLAVE=0x0703

bus=1
fr = io.open("/dev/i2c-"+str(bus), "rb", buffering=0)
fw = io.open("/dev/i2c-"+str(bus), "wb", buffering=0)

# set device address
fcntl.ioctl(fr, I2C_SLAVE, I2C_address)
fcntl.ioctl(fw, I2C_SLAVE, I2C_address)
time.sleep(0.015) #15ms startup time

def getInfo(Number):
	if ((Number >= 0) and (Number <= 3)):
		address = moduleAddress + Number
		address2 = moduleAddress2 + Number
		address1 = moduleAddress1
		#check address
		testaddr = (address1<<16) + address2
		if address != testaddr:
			print "ERROR: Device address is not correct!"
			address1 = -1
			address2 = -1
			
	else:
		address = -1
	
	IOdata = wiringdata.getWiring(address)
	datas = [address1,address2]
	datas.extend(IOdata)
	return datas

def getAddr(Number):
	address = -1
	if ((Number >= 0) and (Number <= 3)):
		address = moduleAddress2 + Number
	else:
		address = -1

	return moduleAddress1,moduleAddress2

def getIOs():
	#IOdata = [p.CE1]
	#print "moduleAddress =",moduleAddress 
	IOdata = wiringdata.getWiring(moduleAddress)

	return IOdata


def writeByte(data):
	s = [data]
	s2 = bytearray( s )
	fw.write( s2 )

def writeWord(data1,data2):
	s = [data1,data2]
	s2 = bytearray( s )
	fw.write( s2 )

def readData(num):
	data = fr.read(num) #read 2 byte temperature data
	buf = array.array('B', data)
	
	#print "read test = ",hex(buf[0]),",",hex(buf[1])

	return buf

def read2Data():
	buf = readData(2)
	data = (buf[0] << 8) | buf[1]
	#print "data = ",hex(data) 
	return data

def readLE():
	buf = readData(2)
	data = (buf[1] << 8) | buf[0]
	#print "data = ",hex(data) 
	return data

def getCalibData():
	
	data = []
	
	#big_T
	writeByte(0x88)
	buf = readLE()
	data.append(buf)
	
	writeByte(0x8A)
	buf = readLE()
	data.append(buf)
	
	writeByte(0x8C)
	buf = readLE()
	buf = (0xFFFF0000 + buf)
	buf = -1*(0xFFFFFFFF - buf + 1)
	#print "buf = ",buf
	data.append(buf)
	
	
	#big_P
	writeByte(0x8E)
	buf = readLE()
	data.append(buf)
	
	writeByte(0x90)
	buf = readLE()
	buf = (0xFFFF0000 + buf)
	buf = -1*(0xFFFFFFFF - buf + 1)
	#print "buf = ",buf
	data.append(buf)
	
	#P3
	writeByte(0x92)
	buf = readLE()
	data.append(buf)
	
	writeByte(0x94)
	buf = readLE()
	data.append(buf)
	
	writeByte(0x96)
	buf = readLE()
	data.append(buf)
	
	#P6
	writeByte(0x98)
	buf = readLE()
	buf = (0xFFFF0000 + buf)
	buf = -1*(0xFFFFFFFF - buf + 1)
	#print "buf = ",buf
	data.append(buf)
	
	writeByte(0x9A)
	buf = readLE()
	data.append(buf)
	
	#P8
	writeByte(0x9C)
	buf = readLE()
	buf = (0xFFFF0000 + buf)
	buf = -1*(0xFFFFFFFF - buf + 1)
	#print "buf = ",buf
	data.append(buf)
	
	writeByte(0x9E)
	buf = readLE()
	data.append(buf)
	
	#print "data = ",data
	
	time.sleep(0.045)
	return data
	
def read16_LE(reg):
	temp = read16(reg)

def read(data):
	writeWord(0xF4,0x5D)
	time.sleep(0.045)
	
	writeByte(0xF7)
	time.sleep(0.045)
	
	buf = readData(6)
	
	
	
	#print "read test = ",hex(buf[0]),",",hex(buf[1]),",",hex(buf[2]),",",hex(buf[3]),",",hex(buf[4]),",",hex(buf[5])
	uP = ((buf[0]*256.0) + buf[1] + (buf[2]/256.0)) * 16.0
	uT = ((buf[3]*256.0) + buf[4] + (buf[5]/256.0)) * 16.0
	#print "uP = ",uP," uT = ",uT
	
	#temp
	var1 = (uT / 16384.0 - (data[0] / 1024.0)) * data[1]
	#print "var1 = ",var1
	var2 = ((uT / 131072.0 - (data[0] / 8192.0)) * (uT / 131072.0) - (data[0] / 8192.0)) * data[2]
	#print "var2 = ",var2
	t_fine = round((var1 + var2),0)
	#print "t_fine = ",t_fine
	
	T = (var1 + var2)/5120.0
	#print "T = ",T
	
	#pressure
	var1 = (t_fine / 2.0) - 64000.0
	var2 = var1 * (var1 * (data[8] / 32768.0))
	var2 = var2 + (var1 * (data[7] * 2.0))
	var2 = (var2 / 4.0) + (data[6] * 65536.0) 
	var1 = ((data[5]) * var1 * var1 / 524288.0 + (data[4]) * var1) / 524288.0
	t_var = (32768.0 + var1) / 32768.0
	tt_var = t_var * data[3]
	var1 = ((32768.0 + var1) / 32768.0) * data[3]
	p = 1048576.0 - uP
	p = (p - (var2/4096.0))*6250.0/var1
	var1 = data[11] * p * p / 2147483648.0
	var2 = p * data[10] / 32768.0
	p = p + (var1 + var2 + data[9]) / 16.0
	P = p / 100.0
	#print "P = ",P
	
	#Altitude
	A = 44330.0 * (1-((P/1013.25)**(1/5.255)))
	
	return T,P,A
	
def readAir():
	buf = read24Data()
	temp = buf[0]
	temp |= temp
	
	
	s = [0x00] # temp
	s2 = bytearray( s )
	fw.write( s2 )
	time.sleep(0.0625)              # From the data sheet

	data = fr.read(2) #read 2 byte temperature data
	buf = array.array('B', data)
	rawData = ((buf[0]<<8) + (buf[1]))
	Temp = (((rawData/65536.0)*165.0 ) - 40.0) 

	time.sleep(0.015)               # From the data sheet
	return Temp,rawData
	
def readHumidity():
	
	s = [0x01] # hum
	s2 = bytearray( s )
	fw.write( s2 )
	time.sleep(0.0625)              # From the data sheet

	data = fr.read(2) #read 2 byte temperature data
	buf = array.array('B', data)
	rawData = ((buf[0]<<8) + (buf[1]))
	Humidity = ((rawData/65536.0)*100.0 ) 
	return Humidity, rawData
	
def cleanup():
	i2c.close()
