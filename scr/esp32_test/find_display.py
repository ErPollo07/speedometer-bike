from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

devices = i2c.scan()
if devices:
    print("Dispositivi trovati:", [hex(d) for d in devices])
else:
    print("Nessun dispositivo trovato sul bus I2C")

