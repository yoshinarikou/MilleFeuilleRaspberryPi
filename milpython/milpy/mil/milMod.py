import struct
import mil
import time
import p
DEF_LOCATION = 18
class milMod():
	
	
	#def __init__(self, addr1):
	#def __init__(self, bank, addr1, *pinData1):
	#def __init__(self, addr1,addr2, pinData1):
		
	def __init__(self, datas):
		addr1 = datas[0]
		addr2 = datas[1]
		
		datas.remove(addr1)
		datas.remove(addr2)
		print "milMod ini datas = ",datas
		pinData1 = datas
		
		self.addr = (addr1<<16) + addr2
		self.addr1 = addr1
		self.addr2 = addr2
		#print "self.addr = ",hex(self.addr)
		self.BANK = 1
		self.location = 255
		self.DIR = [0,0,0,0,0,0,0,0]
		self.secondDIR = [0,0,0,0,0,0,0,0]
		#self.mDIR = 0x00
		print "pinData1 = ",pinData1
		
		self.pinData = []
		self.secondPinData = []
		
		for var in range(0, len(pinData1)):
			self.pinData.append(pinData1[var])
			
		for var in range(0, len(pinData1)):
			self.secondPinData.append(pinData1[var])
			
		#self.pinData = pinData1
		#print "self.pinData = ",self.pinData
		#self.secondPinData  = pinData1
		#print "self.pinData = ",self.pinData
		#print "self..secondPinData = ",self.secondPinData
		
		self.getSecondPins()
		
		#if self.pinData[0] == p.io[0]:
			 
		#self.doublePinData[0] = pinData1[0]
		
		
		#print "self.pinData = ",self.pinData
		#print "self..secondPinData = ",self.secondPinData
		
		#Uart detect
		flg_uartDev = 0
		#detect address = read baseboard
		for var in range(0, len(pinData1)):
			if (pinData1[var] == p.Tx) or (pinData1[var] == p.Rx):
				#UART devices
				self.location = 17 #device
				self.pinTypeData = 0x03
				flg_uartDev = 1
		
		print "flg_uartDev = ",flg_uartDev
		
		if flg_uartDev == 1:
			mil.getUartAddr()
		
		if flg_uartDev == 0:
			#Normal detect
			self.location = mil.detectModule(self.addr1,self.addr2)
			#self.location = 1

			print "location = ",self.location
			if self.location  == 255:
				tempaddr = (addr1<<16) + addr2
				tempaddr = tempaddr - 0x80000000
				location = tempaddr % 4
				print "Detect Error : Try estimated location = ",location
					
		#self.setPinData(*self.pinData)
		self.setPinData(self.pinData)
		self.setSecondPinData(self.secondPinData)
		self.pinTypeData = self.setPinType(self.pinData)
		
		#self.regBank(self.BANK)
		print "end Milmod init"
		
		

	def regBank(self,bank):
	#def regBank(self,bank, pinOffset):
		if self.addr != -1:
			flg_uartPin = 0
			for var in range(0,len(self.pinData)):
				#print "var = ",var 
				#if((self.pinData[var] == p.SDA)or(self.pinData[var] == p.SCL)or(self.pinData[var] == p.NC)or(self.pinData[var] == p.Tx)or(self.pinData[var] == p.Rx)):
				if((self.pinData[var] == p.SDA)or(self.pinData[var] == p.SCL)or(self.pinData[var] == p.NC)):
					#nothin to do
					print "ignore"
					self.pinData[var] = self.pinData[var]
				elif ((self.pinData[var] == p.Tx)or(self.pinData[var] == p.Rx)):
					print "uart pin"
					flg_uartPin = 1
					
				else:
					tempLocation = self.location + var	#InOutpin
					print "tempLocation = ",tempLocation, " self.DIR[",var,"] = 0x",hex(self.DIR[var])
					if tempLocation <= DEF_LOCATION:
						mil.writeBase(tempLocation, self.DIR[var])	#set wiring
			

	def cutWire(self):
		if self.addr != -1:
			for var in range(0,len(self.pinData)):
				#print "var = ",var 
				tempLocation = self.location + var	#InOutpin
				#print "tempLocation = ",tempLocation, " self.DIR[",var,"] = 0x00"
				if tempLocation <= 16:
					mil.writeBase(tempLocation, 0x00)	#cut wiring
			

				

	#def setPinData(self, *pinData1):
	def setPinData(self, pinData1):
		
		if self.addr != -1:

			#print("setPinData\n")
			#print self.pinData
		
			#check Pin Direction
			#print "self.pinData",self.pinData
			for var in range(0,len(self.pinData)):
				

				for var2 in range(0,len(p.inpin)):
					if self.pinData[var] == p.inpin[var2]:
						print "p.inpin[",var2,"] = ",p.inpin[var2]
						self.DIR[var] = var2 + 0x11
						print "var = ",var ," var2 = ",var2 ," self.DIR[",var,"] = ", hex(self.DIR[var])

				for var2 in range(0,len(p.outpin)):
					if self.pinData[var] == p.outpin[var2]:
						print "p.outpin[",var2,"] = ",p.outpin[var2]
						self.DIR[var] = var2 + 0x01
						print "var = ",var ," var2 = ",var2 ," self.DIR[",var,"] = ", hex(self.DIR[var])
				
			
				if self.pinData[var] == p.CE1:
					self.DIR[var] = 9
					print "p.CE1 self.DIR[",var,"] = ",self.DIR[var]
				if self.pinData[var] == p.NC:
					self.DIR[var] = 255

	def setPinType(self, pinData1):
		#MOSI,MISO,SCLK
		if self.pinData[0] == p.MOSI and self.pinData[1] == p.MISO and self.pinData[2] == p.SCLK:
			pinTypeData = 0x07
		elif self.pinData[0] == p.MOSI and self.pinData[1] != p.MISO and self.pinData[2] == p.SCLK:
			pinTypeData = 0x08
		elif self.pinData[0] != p.MOSI and self.pinData[1] == p.MISO and self.pinData[2] == p.SCLK:
			pinTypeData = 0x0A
		#elif self.pinData[0] != p.MOSI and self.pinData[1] != p.MISO and self.pinData[2] == p.SCLK:
		#	pinTypeData = 0x0A
		else:
			pinTypeData = 0x02
			
		print "setPinType : 0x",hex(pinTypeData)
		
		return pinTypeData

	def connect(self):
		#print "connect regBANK = ",self.BANK
		#mil.changeBank(self.BANK)
		print "connect!"
		self.regBank(self.BANK)
		if self.pinTypeData != 0x03:
			mil.openModule(self.addr1,self.addr2,self.pinTypeData)
	
	def disconnect(self):
		mil.closeModule(self.addr1,self.addr2)
		self.cutWire()
		#mil.detectEnd()
	
	def getSecondPins(self):
		#print "self.pinData = ",self.pinData
		#serch inpin
		
		print "1self.pinData = ",self.pinData
		print "1self.secondPinData = ",self.secondPinData
		
		for var in range(0, len(self.pinData)):
			if self.pinData[var] == p.inpin[var]:
				self.secondPinData[var] = p.inpin[var + 4]
			else:
				self.secondPinData[var] = self.pinData[var]
		
		var = 0
		#serch outpin
		for var in range(0, len(self.pinData)):
			#print "var = ",var
			if self.pinData[var] == p.outpin[var]:
				self.secondPinData[var] = p.outpin[var + 4]
				print "self.secondPinData[",var,"] = ", self.secondPinData[var] ,":p.outpin[",(var + 4),"] = ",p.outpin[var + 4]
				print "1.5self.pinData = ",self.pinData 
	
		
		print "2self.pinData = ",self.pinData
		print "2self.secondPinData = ",self.secondPinData
		
		
	def setSecondConnect(self, secondPinData):
		self.secondPinData = secondPinData
		
	def secondConnect(self):
		print "second connect!"
		self.regSecondBank(self.BANK)
		mil.openModule(self.addr1,self.addr2,self.pinTypeData)
		

	def regSecondBank(self,bank):
		if self.addr != -1:
			for var in range(0,len(self.secondPinData)):
				#print "var = ",var 
				if((self.secondPinData[var] == p.SDA)or(self.secondPinData[var] == p.SCL)or(self.secondPinData[var] == p.NC)or(self.secondPinData[var] == p.Tx)or(self.secondPinData[var] == p.Rx)):
					#nothin to do
					print "ignore"
					self.secondPinData[var] = self.secondPinData[var]
				else:
					tempLocation = self.location + var	#InOutpin
					print "tempLocation = ",tempLocation, " self.DIR[",var,"] = 0x",hex(self.secondDIR[var])
					if tempLocation <= DEF_LOCATION:
						mil.writeBase(tempLocation, self.secondDIR[var])	#set wiring
						
	
	
	
	def setSecondPinData(self, pinData1):
		
		if self.addr != -1:

			for var in range(0,len(self.secondPinData)):				

				for var2 in range(0,len(p.inpin)):
					if self.secondPinData[var] == p.inpin[var2]:
						print "p.inpin[",var2,"] = ",p.inpin[var2]
						self.secondDIR[var] = var2 + 0x11
						print "var = ",var ," var2 = ",var2 ," self.secondDIR[",var,"] = ", hex(self.secondDIR[var])

				for var2 in range(0,len(p.outpin)):
					if self.secondPinData[var] == p.outpin[var2]:
						print "p.outpin[",var2,"] = ",p.outpin[var2]
						self.secondDIR[var] = var2 + 0x01
						print "var = ",var ," var2 = ",var2 ," self.secondDIR[",var,"] = ", hex(self.secondDIR[var])
				
			
				if self.secondPinData[var] == p.CE1:
					self.secondDIR[var] = 9
					print "p.CE1 self.secondDIR[",var,"] = ",self.secondDIR[var]
				if self.secondPinData[var] == p.NC:
					self.secondDIR[var] = 255


#def HoldOn(address1,address2):
#	mil.writeModule(address1,address2,0x0B,0xFF)
	
#def HoldOff(address1,address2):
#	mil.writeModule(address1,address2,0x0C,0xFF)

	def HoldOn(self,gate):
		#mil.writeModule(self.addr1,self.addr2,0x0B,0xFF)
		mil.writeModule(self.addr1,self.addr2,0x0B,gate)
		
	def HoldOff(self):
		mil.writeModule(self.addr1,self.addr2,0x0C,0xFF)
	
