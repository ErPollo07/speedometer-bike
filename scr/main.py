from machine import Pin, SoftI2C
import ssd1306
import time

WIDTH = 128
HEIGHT = 64

SPOKE_COUNT = 4         # numero di raggi
WHEEL_CIRC  = 1         # circonferenza ruota 16" in metri
INTERVAL_MS = 500

sensor = Pin(34, Pin.IN)

i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

elapsed     = 0
last_pulse = time.ticks_ms()
speed_kmh   = 0.0
last_check = time.ticks_ms()

def on_pulse(pin):
    global elapsed, last_pulse, speed_kmh, last_check
    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, last_pulse)

    last_pulse, last_check = now, now
    
    t = elapsed / 1000
    space = WHEEL_CIRC / SPOKE_COUNT
    speed_kmh = (space / t) * 3.6
    print("{:.3f} m / {:.3f} s = {:.3f} km/h".format(space, t, speed_kmh))


# IRQ_FALLING = scatta quando il raggio viene interrotto (HIGH→LOW)
sensor.irq(trigger=Pin.IRQ_FALLING, handler=on_pulse)

while True:
    now     = time.ticks_ms()
    elapsed = time.ticks_diff(now, last_check)

    # Decrease the speed if more that INTERVAL_MS is passed between now and the last pulse
    if elapsed >= INTERVAL_MS:
        last_check = now
        speed_kmh = speed_kmh - 0.5 if speed_kmh >= 0.5 else 0

    print("Velocita': {:.3f} km/h".format(speed_kmh))

    oled.fill(0)
    oled.text("{:.3f} km/h".format(speed_kmh), 28, 32)
    oled.show()

    time.sleep_ms(50)
