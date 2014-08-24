import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT) ## Setup GPIO Pin 18 to OUT
GPIO.output(23,True) ## Turn on GPIO pin 18
