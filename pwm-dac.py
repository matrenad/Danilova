import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


try:
    pwm = GPIO.PWM(21, 1000)
    pwm2 = GPIO.PWM(22, 1000)
    pwm.start(0)
    pwm2.start(0)
    while True:
        x = int(input())
        print('{:.2f}'.format(x/100*3.3) + 'V')
        pwm.start(x)
        pwm2.start(x)

finally: 
    pwm.stop()
    pwm2.stop()  
    GPIO.cleanup()