from machine import Pin, SoftI2C
import ssd1306
import time

WIDTH = 128
HEIGHT = 64

i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

for i in range(0, 58):
    oled.fill(0)
    oled.text("Test", 0, i)
    oled.show()
    time.sleep_ms(100)