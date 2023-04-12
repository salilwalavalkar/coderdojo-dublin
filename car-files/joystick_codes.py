#setup stuff, dont need to edit the below

import time
from evdev_uart import Evdev

def handleJoystick(joystick_event_type, joystick_event_code, joystick_event_value):
    #you can start here!
    
    print( "Joystick event code was: " + str(joystick_event_code))
    print( "Joystick event value was: " + str(joystick_event_value))

#more setup stuff, dont need to edit the below
if __name__ == "__main__":
    evdev = Evdev(handleJoystick)
    while True:
        evdev.loop()