#This program was written by Justin Suess and is freely available under
#the terms of the GNU Public Liscence v3. (GPLv3)
#
#
#

import pygame

class JoystickReader:
	joy = 0
        discon = False 
	#initializes the joystick module
	def __init__(self):
                self.tryConnect()
        def tryConnect(self):
                try:
                    self.joy.get_axis(0)
                    return True
                except:
                    try:
                        pygame.joystick.quit()
		        pygame.joystick.init()
		        pygame.joystick.Joystick(0).init()
		        self.joy = pygame.joystick.Joystick(0)
                        self.Discon = False
                        return True
                    except Exception as ex:
                        print(ex)
                        self.Discon = True
                        return False

	#Returns the name of the joystick
	def getName(self):
		return self.joy.get_name()	
	
	#returns the value of the axis number specified
	def getAxis(self, axisnumber):
                try:
	            return self.joy.get_axis(axisnumber)
                except:
                    return 0

