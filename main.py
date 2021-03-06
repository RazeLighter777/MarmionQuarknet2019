#This program was written by Justin Suess and is freely available under
#the terms of the GNU Public Liscence v3. (GPLv3)
#
#
#
#
import pygame 

from time import sleep
from joystick import JoystickReader
from motorarray import MotorArray	
#This function marks the initial starting point for the program
def main():

	#Initialize the motor array with the correct port numbers
	motors = MotorArray(4,5,6,13)

	#Start up the pygame module
	pygame.init()

	#create the joystick reader
	joy = JoystickReader()
        
        while True:
            counter = 0
	    while True:
                counter += 1
                if ((counter % 10) == 0):
                    if (joy.tryConnect() == False):
                        break
		pygame.event.get()
		
		print(joy.getAxis(0))
		print(joy.getAxis(1))


		if joy.getAxis(0) > 0.5:
			motors.switchOn(1)
		else:
			motors.switchOff(1)
		
		if joy.getAxis(0) < -0.5:
			motors.switchOn(2)
		else:
			motors.switchOff(2)

		if joy.getAxis(1) > 0.5:
			motors.switchOn(3)
		else:
			motors.switchOff(3)

		if joy.getAxis(1) < -0.5:
			motors.switchOn(4)
		else:
			motors.switchOff(4)	
                sleep(0.05)
	    print("Disconnect!!")

#call the main function	
main()
