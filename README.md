mille-feuille hardware library for Raspberry Pi.
====
Overview
http://milletool.com/

![Overview](http://milletool.com/img/HardAll.jpg)


## Description
The mille-feuille is a support tool making electronic schematic for programmers.

## Demo
https://www.youtube.com/watch?v=unjAE7fYMFo

## Features
- Automatic wiring system firmware library.
- It can detect connected hardware compornents and generate hardware information for creating electronic shematic and its firmware.

## Requirement
- mille-feuille board(Baseboard, module board, Flexible flat cable, Device boards)
- Raspberry Pi A+, B+, 2, 3, Zero.
- SPI and I2C must be enable.

## Install
- Just download these files. 
$git clone git://github.com/yoshinarikou/MilleFeuilleRaspberryPi.git

$cd MilleFeuilleRaspberryPi

$cd milpython

Turn on the mille-feuille and push reset button.
Run sample programs.
$sudo python -B ***Test.py

## Usage
Just run the python script.
Command is $sudo python -B ***.py

To run sample programs.
Directry is ~/milpython/***Test.py

To make circuit information. 
Directry is ~/milpython/detect.py 

## Contribution
Everyone can join this project.
We are going to prepare for registing device boards address.

## Author

[yoshinarikou](https://github.com/yoshinarikou)
