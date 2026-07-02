from machine import Pin, PWM
import time, _thread

pin = Pin(21, Pin.OUT)

pwm = PWM(Pin(19), freq=5000)

def blink():
    while True:
        pin.value(1)
        time.sleep(1)
        pin.value(0)
        time.sleep(1)

def fade():
    while(True):
            pwm.duty(i)
            time.sleep_ms(1)
            
        for i in range(1023, -1, -1):
            pwm.duty(i)
            time.sleep_ms(1)
        
        time.sleep_ms(10)


_thread.start_new_thread(blink, ())
fade()