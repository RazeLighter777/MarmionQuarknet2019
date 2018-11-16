#This program was written by Justin Suess and is freely available under
#the terms of the GNU Public Liscence v3. (GPLv3)
#
#
#

import pygame

class JoystickReader:
	joy = 0
	#initializes the joystick module
	def __init__(self):
		pygame.joystick.init()
		pygame.joystick.Joystick(0).init()
		self.joy = pygame.joystick.Joystick(0)

	#Returns the name of the joystick
	def getName(self):
		return self.joy.get_name()	
	
	#returns the value of the axis number specified
	def getAxis(self, axisnumber):
		return self.joy.get_axis(axisnumber)
	
