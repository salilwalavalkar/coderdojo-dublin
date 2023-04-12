#setup stuff, dont need to edit the below
import time
from machine import Pin, I2C
from pico_car import SSD1306_I2C, ultrasonic, ws2812b
ultrasonic = ultrasonic()
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
num_leds = 8  
pixels = ws2812b(num_leds, 0)

#you can start here!
while True:
    #get distance
    distance = ultrasonic.Distance_accurate()
    
    #display distance
    oled.text('distance:', 0, 0)
    oled.text(str(distance), 75, 0)
    oled.show()
    oled.fill(0)

    #if less than 20 then red, otherwise green
    if( distance < 20 ):
        pixels.fill(50, 0, 0)
        pixels.show()
    else:
        pixels.fill(0, 50, 0)
        pixels.show()

    time.sleep(0.25)
