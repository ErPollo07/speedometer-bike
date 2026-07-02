from machine import Pin, SoftI2C
import ssd1306
import time

WIDTH = 128
HEIGHT = 64

SPOKE_COUNT = 4         # numero di raggi
WHEEL_CIRC  = 1         # circonferenza ruota 16" in metri
INTERVAL_MS = 500       # ogni quanti ms calcola la velocità

sensor = Pin(34, Pin.IN)

i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

pulse_count  = 0
speed_kmh    = 0.0
max_speed    = 0.0
last_calc    = time.ticks_ms()

def on_pulse(pin):
    global pulse_count
    pulse_count += 1

# IRQ_FALLING = scatta quando il raggio viene interrotto (HIGH→LOW)
sensor.irq(trigger=Pin.IRQ_FALLING, handler=on_pulse)

while True:
    now     = time.ticks_ms()
    elapsed = time.ticks_diff(now, last_calc)

    if elapsed >= INTERVAL_MS:
        # "congela" il contatore e lo azzera subito
        count       = pulse_count
        pulse_count = 0
        last_calc   = now

        # calcolo velocità
        pulses_per_sec = count / (elapsed / 1000)
        rps            = pulses_per_sec / SPOKE_COUNT
        speed_kmh      = rps * WHEEL_CIRC * 3.6

        # aggiorna il massimo
        # if speed_kmh > max_speed:
        #     max_speed = speed_kmh

        print("Velocita': {:.1f} km/h | rps: {:.3f} | pps: {:.3f}".format(speed_kmh, rps, pulses_per_sec))
        oled.fill(0)
        oled.text("{:.1f} km/h".format(speed_kmh, max_speed), 28, 32)
        oled.show()

    time.sleep_ms(2)
