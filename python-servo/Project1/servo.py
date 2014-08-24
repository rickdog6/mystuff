import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

p = GPIO.PWM(4,50)
p.start(7.5)

try:
        while True:
#		GPIO.output(18,True)                  
		p.ChangeDutyCycle(7.5)
                time.sleep(0.5)
#		GPIO.output(18,False)
#               GPIO.output(23,True)
		p.ChangeDutyCycle(12.5)
                time.sleep(0.5)
#		GPIO.output(23,False)
#		GPIO.output(24,True)
                p.ChangeDutyCycle(3.5)
                time.sleep(0.5)
#		GPIO.output(24,False)
#		GPIO.output(25,True)
                p.ChangeDutyCycle(10.5)
                time.sleep(0.5)
#		GPIO.output(25,False)

except KeyboardInterrupt:
        p.stop()

        GPIO.cleanup()

