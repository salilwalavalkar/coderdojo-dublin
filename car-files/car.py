from evdev_uart import Evdev

from machine import Pin, UART, I2C, PWM, Timer
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

Motor = pico_car()
Motor.Car_Stop()

import time

speed_fwd = 0
speed_back = 0
wheel_angle = 0.0
wheel_count = 0

def handleJoystick(cmd, val):
    global speed_fwd
    global speed_back
    global wheel_angle
    global wheel_count

    if cmd == Evdev.LTRIG:
        speed_back = val
    elif cmd == Evdev.RTRIG:
        speed_fwd = val
    elif cmd == Evdev.XAXIS:
        if val < 32768:
            wheel_angle = val
        else:
            wheel_angle = 32767 - val

    if wheel_angle < 0:
# normal mode, the yahboom car drives better in reverse lol
#        wheel_left = int( (speed_fwd - speed_back) * (-wheel_angle/32767) )
#        wheel_right = int( speed_fwd - speed_back )
        wheel_right = int( (speed_fwd - speed_back) * (-wheel_angle/32767) )
        wheel_left = int( speed_fwd - speed_back )
    else:
# normal mode
#        wheel_left = int( speed_fwd - speed_back )
#        wheel_right = int( (speed_fwd - speed_back) * ((32768-wheel_angle)/32767) )
        wheel_right = int( speed_fwd - speed_back )
        wheel_left = int( (speed_fwd - speed_back) * ((32768-wheel_angle)/32767) )

    if speed_fwd > speed_back:
# normal mode
#        Motor.Car_Run(wheel_left,wheel_right)
        Motor.Car_Back(wheel_left,wheel_right)
    else:
# normal mode
#        Motor.Car_Back(-wheel_left,-wheel_right)
        Motor.Car_Run(-wheel_left,-wheel_right)

if __name__ == "__main__":
    uart = machine.UART(0, 115200)
    uart = UART(0, 115200, tx=Pin(16), rx=Pin(17))

    print(uart)

    evdev = Evdev(handleJoystick)
    
    while True:
        if uart.any():
            b = uart.read(5)
            evdev.handleUdp(b)
