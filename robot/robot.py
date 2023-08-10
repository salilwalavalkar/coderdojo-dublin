# Simplified version of pico_car.py
# To allows young students to understand the code
# that uses these functionalities

import time
from machine import Pin, PWM, I2C
from evdev_uart import Evdev

from pico_car import SSD1306_I2C, pico_car, ws2812b, ultrasonic


RUNNING = True

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NONE = (0, 0, 0)

TEXT_FIRST_LINE = 0
TEXT_SECOND_LINE = 18


# Robot Pulse Width Modulation (PWM)
joystick_events = None
rotors = None
buzzer = None
ultrasound = None
display = None
lights = None


def wait(secs: float = 1.0):
    """
    Wait for a given amount of time.
    
    Parameters
    ----------
    time : int
        The amount of time to wait in seconds.
    """
    time.sleep(secs)

def turn_on():
    """
    Initialise the robot rotors
    """
    global joystick_events, rotors, buzzer, ultrasound, display, lights

    rotors = pico_car()
    stop()

    joystick_events = Evdev(handle_joystick)

    buzzer = PWM(Pin(22))
    buzzer.freq(1000)
    buzzer.duty_u16(0)

    ultrasound = ultrasonic()

    i2c = I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
    display = SSD1306_I2C(128, 32, i2c)
    clear_message()
    
    lights = ws2812b(8, 0)
    lights_off()

def turn_off():
    """
    Turn off the robot rotors
    """
    buzzer.duty_u16(0)
    stop()
    lights_off()
    clear_message()
    display.poweroff()
    
def use_joystick():
    """
    Use the joystick to control the robot
    """
    joystick_events.loop()


# ROTORS ----------------------------------------------------------------------

def stop():
    """
    Stop all rotors
    """
    rotors.Car_Stop()

def forward(speed: int = 250):
    """
    Move the robot forward
    
    Parameters
    ----------
    speed : int
        The speed to move forward at
    """
    rotors.Car_Run(speed, speed)

def backwards(speed: int = 100):
    """
    Move the robot backwards
    
    Parameters
    ----------
    speed : int
        The speed to move backwards at
    """
    rotors.Car_Back(speed, speed)

def left(speed: int = 150):
    """
    Move the robot left
    
    Parameters
    ----------
    speed : int
        The speed to move left at
    """
    rotors.Car_Left(speed, speed)

def right(speed: int = 150):
    """
    Move the robot right
    
    Parameters
    ----------
    speed : int
        The speed to move right at
    """
    rotors.Car_Right(speed, speed)
    
def spin():
    """
    Spin the robot
    
    Parameters
    ----------
    speed : int
        The speed to spin at
    """
    left(150)
    wait(1)

def handle_joystick(evdev_type, evdev_code, evdev_value):
    """
    Handle joystick events
    
    Parameters
    ----------
    evdev_type : int
        The type of event
    evdev_code : int
        The code of the event
    evdev_value : int
        The value of the event
    """
    # print( "Joystick event code was: " + str(evdev_code))
    # print( "Joystick event value was: " + str(evdev_value))

    if( evdev_code == 706 and evdev_value == 1):
        forward(250)

    elif( evdev_code == 706 and evdev_value == 0):
        stop()
        
    if( evdev_code == 704 and evdev_value == 1):
        right(150)

    elif( evdev_code == 704 and evdev_value == 0):
        stop()
        
    if( evdev_code == 705 and evdev_value == 1):
        left(150)

    elif( evdev_code == 705 and evdev_value == 0):
        stop()
        
    if( evdev_code == 707 and evdev_value == 1):
        backwards(100)

    elif( evdev_code == 707 and evdev_value == 0):
        stop()


# BUZZER ----------------------------------------------------------------------

def sound(frequency: int, volume: int = 500, seconds: float = 0.05):
    """
    Make a sound
    
    Parameters
    ----------
    frequency : int
        The frequency of the sound
    volume : int
        The volume of the sound
    seconds : float
        The length of the sound
    """
    buzzer.duty_u16(volume)
    buzzer.freq(frequency)
    wait(seconds)
    buzzer.duty_u16(0)
    wait(0.05)

def beep():
    """
    Make a beep sound
    """
    sound(1000)


# ULTRASONIC ------------------------------------------------------------------

def distance():
    """
    Get the distance from the ultrasonic sensor
    
    Returns
    -------
    int
        The distance in cm
    """
    return ultrasound.Distance_accurate()


# DISPLAY --------------------------------------------------------------------- 

def message(text: str, row: int = 1):
    """
    Display a message on the OLED display
    
    Parameters
    ----------
    text : str
        The text to display
    """
    if row > 2:
        row = 2
    if row < 1:
        row = 1
    write_message(text, 0, (row - 1) * TEXT_SECOND_LINE)

def write_message(text: str, x: int = 0, y: int = 0):
    """
    Display a message on the OLED display
    
    Parameters
    ----------
    text : str
        The text to display
    """
    display.text(text, x, y)
    display.show()
    #display.fill(0)

def clear_message():
    """
    Clear the OLED display
    """
    display.fill(0)
    display.show()


# LIGHTS ----------------------------------------------------------------------

def lights_on(colour = WHITE):
    """
    Turn on the lights
    """
    for i in range(8):
        lights.set_pixel(i, *colour)
        lights.show()
        wait(0.01)

def lights_off():
    """
    Turn off the lights
    """
    for i in range(8):
        lights.set_pixel(i, *NONE)
        lights.show()
        wait(0.01)

def lights_blink(colour = WHITE, seconds: float = 0.5):
    """
    Blink the lights
    
    Parameters
    ----------
    colour : tuple
        The colour of the lights
    seconds : float
        The length of the blink
    """
    lights_on(colour)
    wait(seconds)
    lights_off()
    wait(seconds)

def lights_circle(colour = WHITE, seconds: float = 0.5):
    """
    Circle the lights
    
    Parameters
    ----------
    colour : tuple
        The colour of the lights
    seconds : float
        The length of the circle
    """
    for i in range(8):
        lights.set_pixel(i, *colour)
        lights.show()
        wait(seconds)
        lights.set_pixel(i, *NONE)
        lights.show()
