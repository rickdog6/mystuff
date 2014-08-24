import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from array import *
a = [18,23,25,24]

for i in range (0,8)
      print "setup pin", a[i]
      GPIO.setup(a[i],GPIO.OUT)
      GPIO.output(a[i],GPIO.HIGH)

count = 0
delay = 0.04

while True:
   print "turning on..."
   for i in range(0,8):
        GPIO.output(a[i],GPIO.LOW)
        time.sleep(delay)
        for (i>0):
             GPIO.output(a[i-1],GPIO.HIGH)
             GPIO.output(a[i],GPIO.HIGH)
        print(i)

   print "done. turning off"
   for i in range(0,8)
        GPIO.output(a[7-i],GPIO.LOW)
         time.sleep(delay)
        for (i>0):
             GPIO.output(a[7-(i-1)],GPIO.HIGH)
             GPIO.output(a[7-i],GPIO.HIGH)
        print(i)

   print "off"

# end of while loop
# notice count never reaches 1, so loops forever
# notice HIGH and LOW reversed in my example (bug in RPi 0.3.0a)
# modify and experiment as necessary
# array used to map the GPIO pins which are various non-continuous numerals to digit 0 to 3