#!/usr/bin/python

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
#p.start(7.5)

def move1():
	GPIO.output(18,GPIO.HIGH)                  
	p.ChangeDutyCycle(7.5)
	time.sleep(1)
	GPIO.output(18,GPIO.LOW)
#	GPIO.cleanup()

def move2():
	GPIO.output(23,GPIO.HIGH)
	p.ChangeDutyCycle(12.5)
	time.sleep(1)
	GPIO.output(23,GPIO.LOW)
#	GPIO.cleanup()

def move3():
	GPIO.output(24,GPIO.HIGH)
	p.ChangeDutyCycle(3.5)
	time.sleep(1)
	GPIO.output(24,GPIO.LOW)
#	GPIO.cleanup()
	
def move4():
	GPIO.output(25,GPIO.HIGH)
	p.ChangeDutyCycle(10.5)
	time.sleep(0.5)
	GPIO.output(25,GPIO.LOW)
#	GPIO.cleanup()


root = Tk()
root.geometry("400x400+300+300")
root.title("Servo & LED Controller")
b1 = Button(root, text='Dir1', command = move1)
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='Dir2', command = move2)
b2.pack(side=LEFT, padx=5, pady=5)
b3 = Button(root, text='Dir3', command = move3)
b3.pack(side=LEFT, padx=5, pady=5)
b4 = Button(root, text='Dir4', command = move4)
b4.pack(side=LEFT, padx=5, pady=5)
b5 = Button(root, text='Quit', command = root.quit)
b5.pack(side=LEFT, padx=5, pady=5)
root.mainloop()
