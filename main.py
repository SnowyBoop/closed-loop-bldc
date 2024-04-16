import RPi.GPIO as GPIO
from time import sleep

# Setup
PIN_A = 12
PIN_B = 11
PIN_SWITCH = 10
PIN_BLDC = 9
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_A, GPIO.IN)
GPIO.setup(PIN_B, GPIO.IN)
GPIO.setup(PIN_SWITCH, GPIO.IN)
GPIO.setup(PIN_BLDC, GPIO.OUT)

position = 0
GPIO.output(PIN_BLDC, GPIO.HIGH)

def read_encoder():
    global position
    if GPIO.input(PIN_A) == GPIO.HIGH:
        if GPIO.input(PIN_B) == GPIO.LOW:
            position += 1
        else:
            position -= 1
    else:
        if GPIO.input(PIN_B) == GPIO.HIGH:
            position += 1
        else:
            position -= 1

try:
    while True:
        read_encoder()
        if position < 0:
            position = 0
        elif position > 180:
            position = 180
        duty_cycle = 2.5 + 10 * position / 180
        GPIO.output(PIN_BLDC, GPIO.HIGH)
        sleep(duty_cycle * 0.001)
        GPIO.output(PIN_BLDC, GPIO.LOW)
        sleep(20 - duty_cycle * 0.001)
finally:
    GPIO.cleanup()
