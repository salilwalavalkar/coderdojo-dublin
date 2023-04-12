#setup stuff, dont need to edit the below

import time
from machine import Pin, PWM
from evdev_uart import Evdev
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

def handleJoystick(evdev_type, evdev_code, evdev_value):
    print( "Joystick event code was: " + str(evdev_code))
    print( "Joystick event value was: " + str(evdev_value))

    #you can start here!
    if( evdev_code == 706 and evdev_value == 1):
        Motor.Car_Run(500,500)

    elif( evdev_code == 706 and evdev_value == 0):
        Motor.Car_Stop()
        
    if( evdev_code == 704 and evdev_value == 1):
        Motor.Car_Right(130,130)

    elif( evdev_code == 704 and evdev_value == 0):
        Motor.Car_Stop()
        
    if( evdev_code == 705 and evdev_value == 1):
        Motor.Car_Left(130,130)

    elif( evdev_code == 705 and evdev_value == 0):
        Motor.Car_Stop()
        
    if( evdev_code == 707 and evdev_value == 1):
        Motor.Car_Back(500,500)

    elif( evdev_code == 707 and evdev_value == 0):
        Motor.Car_Stop()
        
    
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
        evdev.loop()