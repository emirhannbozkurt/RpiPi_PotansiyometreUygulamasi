import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
LED1 = 4
LED2 = 27
LED3 = 22
LED4 = 5
LED5 = 23
LED6 = 13
LED7 = 26
LED8 = 12


GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)
GPIO.setup(LED6,GPIO.OUT)
GPIO.setup(LED7,GPIO.OUT)
GPIO.setup(LED8,GPIO.OUT)

pin_a = 18
pin_b = 24

def discharge():
    GPIO.setup(pin_a, GPIO.IN)
    GPIO.setup(pin_b, GPIO.OUT)
    GPIO.output(pin_b, False)
    time.sleep(0.004)

def charge_time():
    GPIO.setup(pin_b, GPIO.IN)
    GPIO.setup(pin_a, GPIO.OUT)
    count = 0
    GPIO.output(pin_a, True)
    while not GPIO.input(pin_b):
        count = count + 1
    return count

def analog_read():
    discharge()
    return charge_time()

while True:
    k = analog_read()
    if (k <= (1024/8)):
        GPIO.output(LED1,1)
        time.sleep(1)
    else:
        GPIO.output(LED1,0)
        time.sleep(1)
        
    if (k <= (2* 1024/8) and k > (1024/8)):
        GPIO.output(LED2,1)
        time.sleep(1)
    else:
        GPIO.output(LED2,0)
        time.sleep(1)
        
    if (k <= (3* 1024/8) and k > (2* 1024/8)):
        GPIO.output(LED3,1)
        time.sleep(1)
    else:
        GPIO.output(LED3,0)
        time.sleep(1)
        
    if (k <= (4*1024/8) and k > (3* 1024/8)):
        GPIO.output(LED4,1)
        time.sleep(1)
    else:
        GPIO.output(LED4,0)
        time.sleep(1)
        
    if (k <= (5*1024/8) and k > (4* 1024/8)):
        GPIO.output(LED5,1)
        time.sleep(1)
    else:
        GPIO.output(LED5,0)
        time.sleep(1)
        
    if (k <= (6*1024/8) and k > (5* 1024/8)):
        GPIO.output(LED6,1)
        time.sleep(1)
    else:
        GPIO.output(LED6,0)
        time.sleep(1)
        
    if (k <= (7*1024/8) and k > (6* 1024/8)):
        GPIO.output(LED7,1)
        time.sleep(1)
    else:
        GPIO.output(LED7,0)
        time.sleep(1)
        
    if (k <= (8* 1024/8) and k > (7* 1024/8)):
        GPIO.output(LED8,1)
        time.sleep(1)
    else:
        GPIO.output(LED8,0)
        time.sleep(1)