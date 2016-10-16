#!/usr/bin/python

#SPI bus
MISO = 9
MOSI = 10
SCLK = 11
CE0 = 8
CE1 = 7
#CE1(7) is special output pin

#I2C bus
SDA = 2
SCL = 3

#UART
Tx = 14
Rx = 15

NC = 0

io = [17,27,22,5,6,13,19,26,21, 4,20,16,12,25,24,23,18]
inpin = [io[0],io[1],io[2],io[3],io[4],io[5],io[6],io[7],io[8]] #input pin setting [You can change Maximum number and  Pin number]
outpin = [io[9],io[10],io[11],io[12],io[13],io[14],io[15],io[16]]#output pin setting [You can change Maximum number and  Pin number]

#pcbOutput = [17,27,22,5,6,13,19,26,21, 4,20,16,12,25,24,23,18]
#pcbInput = [17,27,22,5,6,13,19,26,21, 4,20,16,12,25,24,23,18]

pcbOutput = [4,17,27,22,5,6,13,19,26, 21,20,16,12,25,24,23,18]
pcbInput = [4,17,27,22,5,6,13,19,26, 21,20,16,12,25,24,23,18]
