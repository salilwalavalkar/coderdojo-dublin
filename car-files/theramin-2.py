#setup stuff, dont need to edit the below
import time
from machine import Pin, I2C, PWM
from pico_car import SSD1306_I2C, ultrasonic, ws2812b
ultrasonic = ultrasonic()
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
num_leds = 8  
pixels = ws2812b(num_leds, 0)

BZ = PWM(Pin(22))
BZ.freq(1000)
BZ.duty_u16(0)

def buzz(num):
    BZ.duty_u16(1000) #volume
    BZ.freq(num*20+20) #note

def light(num):
    i=0
    while i < 8:
        pixels.set_pixel(i, num, 0, 60)
        i += 1

    pixels.show()
 
#you can start here!
while True:
    #get distance
    distance = ultrasonic.Distance_accurate()
    
    #display distance
#     oled.text('distance:', 0, 0)
#     oled.text(str(distance), 75, 0)
#     oled.show()
#     oled.fill(0)

    light(distance)
    buzz(distance)