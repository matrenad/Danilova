import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
for x in dac: GPIO.setup(x, GPIO.OUT)
def dec2bin(n):
    return list(map(int, list((8 - len(bin(n)[2::]))*'0' + bin(n)[2::])))

try:
    period = int(input())
    while True:
        for j in range (256):
            for i in range(8): GPIO.output(dac[i], dec2bin(j)[i])
            time.sleep(period/512)
        for j in range(255, -1, -1):
            for i in range(8): GPIO.output(dac[i], dec2bin(j)[i])
            time.sleep(period/512)
finally:
    for x in dac: GPIO.output(x, 0)
    GPIO.cleanup()