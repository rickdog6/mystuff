import RPi.GPIO as GPIO
import time       

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class LED:                                 
        def __init__(self, color, pin):
                self.color = color.lower()
                if self.color == 'blue':
                        GREEN_LED = pin                          
                        GPIO.setup(GREEN_LED, GPIO.OUT)             
                        self.LED = 'BLUE_LED'                      

                elif self.color == 'red':
                        RED_LED = pin
                        GPIO.setup(RED_LED, GPIO.OUT)
                        self.LED = 'RED_LED'

        def OFF():                           

                GPIO.output(self.LED, False)

        def ON():
                GPIO.output(self.LED, True)


        def flash(repeat=1, length=1, cust=0):  # repeat is automatically 1
                                        # cust is automatically 0
                                        # length is automatically 1:
                                        # 1 = short-on/off for 3sec.
                                        # 2 = medium-on for 5sec. off for 3sec.
                                        # 3 = long-on for 10sec. off for 3 sec.
                                        # 4 = custom-set cust=length on in sec.
                for flash in range(0, repeat):       
                        ON()           
                        if length == '1':
                                time.sleep(3)
                        elif length == '2': 
                                time.sleep(5)
                        elif length == '3':
                                time.sleep(10)
                        elif length == '4':
                                time.sleep(self.cust)
                        OFF()
                        time.sleep(3)                            
                        ON()

        def SOS(repeat=1):
                flash(3, 1)
                flash(3, 3)
                flash(3, 1)                          

def main():                              
        green = LED('blue', 18)

        red = LED('red', 23)                

        green.flash(3)                     
        red.flash(3)                          
try:
	main

except KeyboardInterupt:
	GPIO.cleanup()
