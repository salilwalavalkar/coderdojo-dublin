#setup stuff, dont need to edit the below

import time
from machine import Pin, PWM
from evdev_uart import Evdev
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

def handleJoystick(evdev_type, evdev_code, evdev_value):
    #you can start here!
    pixels.show()

    if( evdev_code == 16 and evdev_value == 65535 ):
        Motor.Car_Left(100,100)

    elif( evdev_code == 16 and evdev_value == 0 ):
        Motor.Car_Stop()
        
    if( evdev_code == 16 and evdev_value == 1 ):
        Motor.Car_Right(100,100)
        
    elif( evdev_code == 16 and evdev_value == 0 ):
        Motor.Car_Stop()
        
        
    if( evdev_code == 17 and evdev_value == 65535 ):
        Motor.Car_Run(500,500)

    elif( evdev_code == 17 and evdev_value == 0 ):
        Motor.Car_Stop()
        
    if( evdev_code == 17 and evdev_value == 1 ):
        Motor.Car_Back(500,500)

    elif( evdev_code == 17 and evdev_value == 0 ):
        Motor.Car_Stop()
    
    # Y
    if( evdev_code == 308 and evdev_value == 1 ):
        pixels.set_pixel(1, 25, 0, 92)
        pixels.set_pixel(4, 25, 0, 92)
        pixels.show()

    elif( evdev_code == 308 and evdev_value == 0 ):
        pixels.set_pixel(1, 0, 0, 0)
        pixels.set_pixel(4, 0, 0, 0)
        pixels.show()
        
    if( evdev_code == 305 and evdev_value == 1 ):
        pixels.set_pixel(2, 25, 0, 92)
        pixels.set_pixel(3, 25, 0, 92)
        pixels.show()

    elif( evdev_code == 305 and evdev_value == 0 ):
        pixels.set_pixel(2, 0, 0, 0)
        pixels.set_pixel(3, 0, 0, 0)
        pixels.show()
        
#more setup stuff, dont need to edit the below
if __name__ == "__main__":
    Motor = pico_car()
    Motor.Car_Stop()
    BZ = PWM(Pin(22))
    BZ.freq(1000)
    BZ.duty_u16(0)
    pixels = ws2812b(8, 0)

    evdev = Evdev(handleJoystick)
    while True:
        evdev.loop();
