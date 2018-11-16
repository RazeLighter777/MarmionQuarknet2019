#This program was written by Justin Suess and is freely available under
#the terms of the GNU Public Liscence v3. (GPLv3)
#
#
#
#
	
#import all necesssary modules

#needed for joystick functionality.
import pygame
#used to control the motors, called LED, but really is just an easy way
#to toggle those GPIO pins
from gpiozero import LED



#this class represents the motors that the pi controls,
class MotorArray:

	#These are the motor objects, initialized to 0	
	motor1 = 0
	motor2 = 0
	motor3 = 0
	motor4 = 0
	
	#Pass in all of the ports for the motors to initialize the system
	def __init__(self, port1, port2, port3, port4):
		self.motor1 = LED(port1)
		self.motor2 = LED(port2)
		self.motor3 = LED(port3)
		self.motor4 = LED(port4)
		
	#This function takes a number (1-4) and turns on the corresponding motor
	def switchOn(self, motornumber):
		if motornumber == 1:
			self.motor1.on()
		elif motornumber == 2:
			self.motor2.on()
		elif motornumber == 3:
			self.motor3.on()
		elif motornumber == 4:
			self.motor4.on()
		else:
			print("Error, that is not a valid motor")

	#This function does the same as above, but turns motors off
	def switchOff(self, motornumber):
		if motornumber == 1:
			self.motor1.off()
		elif motornumber == 2:
			self.motor2.off()
		elif motornumber == 3:
			self.motor3.off()
		elif motornumber ==4:
			self.motor4.off()
		else:
			print("Error, that is not a valid motor")

