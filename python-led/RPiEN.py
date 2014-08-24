#GPIO OUTPUT EMAIL INDICATOR - 2014
#Code by Jordan Fry - http://www.greaterdepth.co.uk
#Lightly based on Adafruit's example code, which they have kindly documented here: http://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview

import RPi.GPIO as GPIO
import time
import sys
import os
import feedparser

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#Specify the pin to activate when email is recieved (in this case GPIO pin 12)
DEVICE = 18
#Declare the output pin as an output
GPIO.setup(DEVICE, GPIO.OUT)
#The following two variables allow you to control the times between which the
#device will flash. This is handy in a bedroom enviroment etc. (24-hours)
START = 060000 
END = 223000
#Gather time at current location and convert to integer
LOCALTIME = int(time.strftime("%H%M%S"))
#Convert both START and END times to integers
START = int(START)
END = int(END)

#This variable controls what happens when an email is recieved
def flash():
         GPIO.output(DEVICE, False)
         time.sleep(1)
         GPIO.output(DEVICE, True)
         time.sleep(1)
 
        
#The following creates a string which retrieves the number of unread emails in your inbox
emails = int(feedparser.parse("https://" + "ricktreinen" + ":" + "querCus12" +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
#If you have more than one inbox which you want to monitor, you can do so using the following code. You can 
#copy this code many times, and replace the username and password each time to add many inboxes.
#(uncomment the following line of code by removing the # sign in order to use it.
#emails = emails + int(feedparser.parse("https://" + "YOUR EMAIL ADDRESS" + ":" + "PASSWORD" +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

#Print the number of emails which are in the inbox (helpful for debugging)
print "You have", emails, "new emails!"

#This if-statment simply says: if there are more than 0 emails and the time is within
#the START and END variable, then execute the code which it contains
if emails > 0 and LOCALTIME > START and LOCALTIME < END:
	#Create a variable to monitor how many times our while statment runs. Also convert it to an integer.
	COUNT = int(0)
	#This allows us to have the actions set out in our function flash() to run as many times as we have emails.
	#It simply checks that there are fewer emails than counts, and adds one to the count variable each time it runs. 
	while (COUNT < emails):
		#Calls function flash()
		flash()
		#Adds one to our COUNT variable
		COUNT = COUNT + 1
	#This turns of the device after it has run as many times as you have emails, so that the LED doesn't remain on
	GPIO.output(DEVICE, False)
	#This exits the code after all of the above has run
	sys.exit() 
#This else variable exits the code if you haven't got any emails to indicate for                       
else:
	#Do nothing
	sys.exit()
