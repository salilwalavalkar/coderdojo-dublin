#setup stuff, dont need to edit the below
import time
from machine import Pin, I2C
from pico_car import SSD1306_I2C, ultrasonic, pico_car, ws2812b
ultrasonic = ultrasonic()
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
num_leds = 8  
pixels = ws2812b(num_leds, 0)
Motor = pico_car()
Motor.Car_Stop()

#you can start here!
while True:
    oled.text('Backwards..', 0, 0)
    oled.show()
    oled.fill(0)
    Motor.Car_Back(100,100)
    time.sleep(1)

    oled.text('Stop..', 0, 0)
    oled.show()
    oled.fill(0)
    Motor.Car_Stop()
    time.sleep(1)

    oled.text('Forwards..', 7000)
    oled.show()
    oled.fill(0)
    Motor.Car_Run(100,100)
    time.sleep(1)
    
    oled.text('Stop..', 0, 0)
    oled.show()
    oled.fill(0)
    Motor.Car_Stop()
    time.sleep(1)

