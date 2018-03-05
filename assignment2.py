#########################################################
# Gregory Gilbert, Chris Major
# assignment2.py
# CSCI 455
# 2/13/2018
#########################################################

from Maestro import Controller
import threading
import tkinter as tk

#def stop(key):
	#Set all servos and motors to stop at neutral position
#def move(key):
	#Change speed of wheels up increases speed by 1, down decreases speed by 1
	#Increase Speed
	#if key.keycode==98:
		#print("up")
		#x.setTarget(0,5000)
		
	
	#Decrease Speed
	#if key.keycode==104:
		#print("down")
	
#def turn(key):
	#Turn the robot using the wheels
	#Left
#	if key.keycode==100:
	
	#Right
#	if key.keycode==102:

	
#def tilt(key):
	#Used to tilt the head up and down
	#Up
#	if key.keycode==87:

	#Down
#	if key.keycode==90:

#def body(key):
	#Used to turn the body left or right, or to center the body.
	#Center
	#if key.keycode==84:
		print("Center")
		x.setTarget(0,6000)

	#Left
	#if key.keycode==83:
		print("Left")
		x.setTarget(0,7000)

	#Right
	#if key.keycode==85:
		print("Right")
		x.setTarget(0,5000)

#def head(key):
	#used to turn the head of the robot left or right, or to center it.
	#Center
#	if key.keycode==80:

	#Left
#	if key.keycode==79:

	#Right
#	if key.keycode==81:


## Main
#con = tk.Tk()
#con.bind('<KP_Enter>',stop)
#con.bind('<Up>',move)
#con.bind('<Down>',move)
#con.bind('<Left>',turn)
#con.bind('<Right>',turn)
#con.bind('<KP_1>',tilt)
#con.bind('<KP_0>',tilt)
#con.bind('<KP_4>',body)
#con.bind('<KP_5>',body)
#con.bind('<KP_6>',body)
#con.bind('<KP_7>',head)
#con.bind('<KP_8>',head)
#con.bind('<KP_9>',head)

#lab = tk.Label(con, text="Hello Tkinter!")

#lab.pack()

x = Controller()
x.setTarget(0, 7800)

con.mainloop()
