# Speedometer

This project is a simple speedometer for any vehicle. It displays the current speed, as well as the maximum speed reached during the current trip.

## Components

### Microcontroller

ESP32, chosen for its compact size, processing power, and built-in Wi-Fi/Bluetooth capabilities.

Freenove ESP32 Kit Dev

### Speed Display

OLED display, controllable via I2C, mounted on the dashboard inside a 3D-printed enclosure.

[Aliexpress](https://it.aliexpress.com/item/1005006141235306.html?spm=a2g0o.cart.0.0.714b18fceknTuP&mp=1&gatewayAdapt=glo2ita)
OLED display 128x64 I2C 0.96 SSD1306 Yellow/Blue

Edit: The display is very small, so have to place a lens in front of it to enlarge the image.

### Speed Sensor

An IR break-beam sensor (separate emitter and receiver) that detects wheel rotation by counting how many times the beam is interrupted by the wheel's spokes. A break-beam design was chosen over a
reflective sensor because the sensor needs to sit 3-5 cm away from the spokes, which is beyond the reliable range of standard reflective IR sensors.

[Aliexpress](https://it.aliexpress.com/item/1005011593903879.html?spm=a2g0o.cart.0.0.4c1218fcuNMuNI&mp=1&gatewayAdapt=glo2ita)
Lamp: 5MM 850 launch
Launch tube power: 1OOmA, transmitting chip 15mil
Lighting method: DC light
Launch angle: Straight
Receiving angle: <10 degrees
Detection method: Through-beam type
Working voltage/current: DC5V/20A
Response time: 2ms
Working temperature: -25 - 60 degrees Celsius
Output mode: NPN normally open
Transmit: Red wire=5VCC black wire=GND
Receive: Red wire = 5VCC black wire = GND white wire = OUT (NPN)
Note: Do not reverse the positive and negative poles of the power supply

## Vehicle specifics

- Motorcycle, 16" wheel rim, 4 spokes.
- Maximum speed: ~70 km/h.

## Links

- [Arduino Tachometer/RPM Meter with IR Sensor Module](https://projecthub.arduino.cc/mircemk/arduino-tachometer-rpm-meter-with-ir-sensor-module-a36d7c)
