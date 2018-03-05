#########################################################
# Gregory Gilbert, Chris Major
# robotMovement.py
# CSCI 455
# 2/13/2018
#########################################################

# IMPORTS

# (C) Import for getch functions
import sys, termios, tty, os, time
from time import sleep

# (C) Import classes and functions from Maestro
from Maestro import Controller

# (C) Key input
def getch():
        #Use standard input
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        # Try connecting standard input
        try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)

        # On successful connection
        finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        # Return stdin        
        return ch    

# (C) Move function
def move(key):
	
	pos = 6000;
	
	# Center body - set speeds and reset all servos
	if (key == "c"):
		print(" >>> Reset All Motors")
		x.setSpeed(0, 60)
		x.setSpeed(1, 50)
		x.setSpeed(2, 50)
		x.setSpeed(3, 60)
		x.setSpeed(4, 60)

		x.setAccel(1, 150)
		x.setAccel(2, 150)

		x.setTarget(0, pos)
		x.setTarget(1, pos)
		x.setTarget(2, pos)
		x.setTarget(3, pos)
		x.setTarget(4, pos)
	
	# Rotate Torso
        if (key == "m"):
                print(" > TORSO - Torso left")	# Rotate Torso Left

		pos = x.getPosition(0) - 1000	

		if (pos > 4000):
			x.setSpeed(0, 60)
			x.setAccel(0, 200)			
			x.setTarget(0, pos)
		else:
			x.setTarget(0, 4000)
	
	if (key == "n"):
		print(" > TORSO - Torso right")	# Rotate Torso Right

		pos = x.getPosition(0) + 1000

		if (pos < 8000):
			x.setSpeed(0, 60)
			x.setAccel(0, 200)
			x.setTarget(0, pos)
		else:
			x.setTarget(0, 8000)     

	# Rotate Head
	if (key == "l"):
		print(" > HEAD - Head turn left")
		
		pos = x.getPosition(3) - 1000	

		if (pos > 4000):
			x.setSpeed(3, 60)
			x.setAccel(3, 200)
			x.setTarget(3, pos)
		else:
			x.setTarget(3, 4000)
	
	if (key == "j"):
		print(" > HEAD - Head turn right")
		
		pos = x.getPosition(3) + 1000	

		if (pos < 8000):
			x.setSpeed(3, 60)
			x.setAccel(3, 200)
			x.setTarget(3, pos)
		else:
			x.setTarget(3, 8000)
	
	# Tilt Head
	if (key == "k"):
		print(" > HEAD - Head tilt up")
		
		pos = x.getPosition(4) - 1000	

		if (pos > 4000):
			x.setSpeed(4, 60)
			x.setAccel(4, 200)
			x.setTarget(4, pos)
		else:
			x.setTarget(4, 4000)
	
	if (key == "i"):
		print(" > HEAD - Head tilt down")
		
		pos = x.getPosition(4) + 1000	

		if (pos < 8000):
			x.setSpeed(4, 60)
			x.setAccel(4, 200)
			x.setTarget(4, pos)
		else:
			x.setTarget(4, 8000)

	# Forward
	if (key == "w"):	
		print("Increment Speed")

		x.setTarget(2, 6000)
	
		#if (pos <= 6000 and pos >= 5350 or pos == 6650):		
		pos = x.getPosition(1) - 650
		#else:
			#pos = x.getPosition(1) - 300
		
		if (pos > 4050):
			x.setSpeed(1, 50)
			x.setAccel(1, 150)
			x.setTarget(1, pos)
		else:
			x.setTarget(1,4050)
		print(" - Speed: %i" % pos)

	# Backward
	if (key == "s"):
		print("Decrement Speed")

		x.setTarget(2, 6000)

		#if (pos >= 6000 and pos <= 6650 or pos == 5350):
		pos = x.getPosition(1) + 650
		#else:
			#pos = x.getPosition(1) + 300
		
		if (pos < 7950):
			x.setSpeed(1, 50)
			x.setAccel(1, 150)
			x.setTarget(1, pos)
		else:	
			x.setTarget(1, 7950)
		print(" - Speed: %i" % pos)

	# Turn Left
	if (key == "a"):
		print("Turn Left")	
		x.setSpeed(2, 50)
		x.setAccel(2, 150)
		x.setTarget(2, 7000)
		sleep(0.5)
		x.setTarget(2, 6000)


	# Turn Right
	if (key == "d"):
		print("Turn Right")
		x.setSpeed(2, 50)
		x.setAccel(2, 150)
		x.setTarget(2, 5000)
		sleep(0.5)
		x.setTarget(2, 6000)


# Initialize key as starter
key = " "

# Create controller object
x = Controller()

# Reset position before starting
x.setTarget(0, 6000)
x.setTarget(3, 6000)
x.setTarget(4, 6000)

print("\nINSTRUCTIONS FOR USE:\n")
print(" W - Increment speed")
print(" S - Decrement speed")
print(" A - Turn left")
print(" D - Turn right\n")
print(" N - Turn torso left")
print(" M - Turn torso right\n")
print(" J - Turn head left")
print(" L - Turn head right")
print(" I - Tilt head up")
print(" K - Tilt head down\n")
print(" C - Center robot, reset all motors:")
print(" Q - Quit, disable robot\n")
print("BEGIN CONTROL\n\n")

# WHILE condition to check key
while key != "q":

	# Get key
	key = getch()

	# Move the bot
	move(key)

# Reset position when we are done
x.setSpeed(0, 60)	
x.setSpeed(1, 50)
x.setSpeed(2, 50)
x.setSpeed(3, 60)
x.setSpeed(4, 60)

x.setAccel(1, 150)
x.setAccel(2, 150)

x.setTarget(0, 6000)
x.setTarget(1, 6000)
x.setTarget(2, 6000)
x.setTarget(3, 6000)
x.setTarget(4, 6000)


print("Robot reset; program ended.")
