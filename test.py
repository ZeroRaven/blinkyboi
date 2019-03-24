import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

ledPin = 4
bttnPin = 17

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(bttnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
buttonPress = True

while True:
    bttnPress = GPIO.input(bttnPin)
    if bttnPress == False:
        GPIO.output(ledPin, True)
        sleep(0.5)
    elif bttnPress == True:
        GPIO.output(ledPin, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(ledPin, GPIO.LOW)
        sleep(0.5)

     
    


