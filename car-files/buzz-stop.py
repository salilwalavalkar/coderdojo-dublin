#setup stuff, dont need to edit the below
import time
from machine import Pin, PWM
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

#more setup stuff, dont need to edit the below
if __name__ == "__main__":
    BZ = PWM(Pin(22))
    BZ.duty_u16(0)
    