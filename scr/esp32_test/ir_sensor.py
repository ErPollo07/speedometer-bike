from machine import Pin
import time

sensor = Pin(34, Pin.IN)

while True:
    if sensor.value() == 0:
        print("Ostacolo rilevato ", sensor.value())
    else:
        print("Nessun ostacolo", sensor.value())

    time.sleep(0.1)