import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

##Define a function named Blink()
def Blink(numTimes,speed):
	for i in range(0,numTimes):## Run loop numTimes
		print "Iteration " + str(i+1)## Print current loop
		GPIO.output(18,True)
		time.sleep(speed)
		GPIO.output(18,False)
		#time.sleep(speed)
		GPIO.output(23,True)
		time.sleep(speed)
		GPIO.output(23,False)
		#time.sleep(speed)
		GPIO.output(25,True)
		time.sleep(speed)
		GPIO.output(25,False)
		#time.sleep(speed)
		GPIO.output(24,True)
		time.sleep(speed)
		GPIO.output(24,False)
		#time.sleep(speed)
	print "Done" ## When loop is complete, print "Done"
	GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))
