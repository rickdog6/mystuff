#!/usr/bin/python
# Tkinter and GPIO together

from Tkinter import *
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.LOW)
GPIO.setup(25,GPIO.OUT)
GPIO.output(25,GPIO.LOW)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,GPIO.LOW)

p = GPIO.PWM(4,50)
p.start(0)

def toggle1():
	if GPIO.input(18):
		p.ChangeDutyCycle(0)
		GPIO.output(18, GPIO.LOW)
#		b1["text"] = "RED"
	else:
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(0)
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
#		b1["text"] = "Turn LED Off"

def toggle2():
	if GPIO.input(23):
		p.ChangeDutyCycle(0)
		GPIO.output(23, GPIO.LOW)
#		b2["text"] = "YELLOW"
	else:
		p.ChangeDutyCycle(12.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(0)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
#		b2["text"] = "Turn LED Off"

def toggle3():
	if GPIO.input(24):
		p.ChangeDutyCycle(0)
		GPIO.output(24, GPIO.LOW)
#		b3["text"] = "GREEN"
	else:
		p.ChangeDutyCycle(3.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(0)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
#		b3["text"] = "Turn LED Off"

def toggle4():
	if GPIO.input(25):
		p.ChangeDutyCycle(0)
		GPIO.output(25, GPIO.LOW)
#		b4["text"] = "BLUE"
	else:
		p.ChangeDutyCycle(10.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(0)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
#		b4["text"] = "Turn LED Off"

def quitRoutine():
	GPIO.cleanup()
	exit()

root = Tk()
root.geometry("620x200+300+300")
root.title("Servo & LED Toggler")
b1 = Button(root, text="RED", command=toggle1)
b1.config(width=12, height=3)
b1.pack(side=LEFT)
b2 = Button(root, text="YELLOW", command=toggle2)
b2.config(width=12, height=3)
b2.pack(side=LEFT)
b3 = Button(root, text="GREEN", command=toggle3)
b3.config(width=12, height=3)
b3.pack(side=LEFT)
b4 = Button(root, text="BLUE", command=toggle4)
b4.config(width=12, height=3)
b4.pack(side=LEFT)



quitButton = Button(root, text="QUIT", command=quitRoutine)
quitButton.config(width=12, height=3)
quitButton.pack(side=LEFT)

root.mainloop()