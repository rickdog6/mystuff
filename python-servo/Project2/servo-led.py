#!/usr/bin/python
# Tkinter and GPIO controlling a servo and LEDs

from Tkinter import *
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)  # This pin connected to servo PWM
GPIO.setup(18,GPIO.OUT)  # The rest are connect to LEDs
GPIO.output(18,GPIO.LOW)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.LOW)
GPIO.setup(25,GPIO.OUT)
GPIO.output(25,GPIO.LOW)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,GPIO.LOW)

p = GPIO.PWM(4,50) # Setting PWM for the servo
p.start(0)  # Starting at 0 keeps it from buzzing while waiting for a button push

def toggle1(r):  # RED
        if GPIO.input(18):
                p.ChangeDutyCycle(0)
                GPIO.output(18, GPIO.LOW)
        else:
                p.ChangeDutyCycle(12.0)
                time.sleep(0.5)  # you can play around with this timing, but this and the next line quiets the servo after moving
                p.ChangeDutyCycle(0)
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(23, GPIO.LOW)  # these next lines turn off all others when one is picked
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)

def toggle2(y):  # YELLOW
        if GPIO.input(23):
                p.ChangeDutyCycle(0)
                GPIO.output(23, GPIO.LOW)
        else:
                p.ChangeDutyCycle(8.5)
                time.sleep(0.4)
                p.ChangeDutyCycle(0)
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)

def toggle3(g):  # GREEN
        if GPIO.input(24):
                p.ChangeDutyCycle(0)
                GPIO.output(24, GPIO.LOW)
        else:
                p.ChangeDutyCycle(4.5)
                time.sleep(0.4)
                p.ChangeDutyCycle(0)
                GPIO.output(24, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)

def toggle4(b):  # BLUE
        if GPIO.input(25):
                p.ChangeDutyCycle(0)
                GPIO.output(25, GPIO.LOW)
        else:
                p.ChangeDutyCycle(1.0)
                time.sleep(0.5)
                p.ChangeDutyCycle(0)
                GPIO.output(25, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)

def quitRoutine(q):     #found that I needed to add this to the quit button so the LEDs would turn off on exit
        GPIO.cleanup()
        exit()

root = Tk()
root.geometry("620x200+300+300")
root.title("Servo & LED Toggler")
root.bind('r',toggle1)
root.bind('y',toggle2)
root.bind('g',toggle3)
root.bind('b',toggle4)

a = toggle1
b = toggle2
c = toggle3
d = toggle4
e = quitRoutine

b1 = Button(root, text="RED", command=lambda: toggle1(a))  #Just happened to have these colors of LEDs, change to whatever you have
b1.config(width=12, height=3)
b1.pack(side=LEFT)
b2 = Button(root, text="YELLOW", command=lambda: toggle2(b))
b2.config(width=12, height=3)
b2.pack(side=LEFT)
b3 = Button(root, text="GREEN", command=lambda: toggle3(c))
b3.config(width=12, height=3)
b3.pack(side=LEFT)
b4 = Button(root, text="BLUE", command=lambda: toggle4(d))
b4.config(width=12, height=3)
b4.pack(side=LEFT)

quitButton = Button(root, text="QUIT", command=lambda: quitRoutine(e))
quitButton.config(width=12, height=3)
quitButton.pack(side=LEFT)
root.bind('q',quitRoutine)

root.mainloop()