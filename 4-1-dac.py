import RPi.GPIO as GPIO
GPIO.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
for x in dac: GPIO.setup(x, GPIO.OUT)
def dec2bin(n):
    return list(map(int, list((8 - len(bin(n)[2::]))*'0' + bin(n)[2::])))

try:
    while True: 
        inp = input()
        if inp == 'q':
            break
        elif sum([inp.count(i) for i in '0123456789']) != len(inp) or (int(inp) > 255):
            print('Введите целое неотрицательное число, не превышающее 255')
        else:
            num = int(inp)
            print('{:.2f}'.format(num/256*3.3) + 'V')
            num_list = dec2bin(num)
            for i in range(8): GPIO.output(dac[i], num_list[i])
finally:
    for x in dac: GPIO.output(x, 0)
    GPIO.cleanup()