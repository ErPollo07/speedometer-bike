from machine import Pin, SoftI2C
import ssd1306
import time

WIDTH = 128
HEIGHT = 64

SPOKE_COUNT = 4        # numero di raggi
WHEEL_CIRC  = 1.277   # circonferenza ruota 16" in metri
INTERVAL_MS = 500     # ogni quanti ms calcola la velocità

sensor = Pin(34, Pin.IN)

i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c) # Questa e' la riga che da problemi

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
        rpm            = rps / 60
        speed_kmh      = (3.14 * 0.54 * rpm * 3.6) / 60

        # aggiorna il massimo
        if speed_kmh > max_speed:
            max_speed = speed_kmh

        print(rpm, rps)
        print("Velocita': {:} km/h  |  Max: {:.1f} km/h".format(speed_kmh, max_speed))
        oled.fill(0)
        text = "{:.1f} km/h".format(speed_kmh)
        oled.text("{}".format(rpm), 56, 0)
        oled.text(text, 32, 29)
        oled.show()

    time.sleep_ms(2)