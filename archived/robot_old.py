# Simplified version of pico_car.py
# To allows young students to understand the code
# that uses these functionalities

import time
import rp2
import framebuf

from machine import Pin, PWM, I2C
from evdev_uart import Evdev


ON = 1
OFF = 0
RUNNING = True

DEFAULT_ROTOR_FREQ = 1000
DEFAULT_ROTOR_SPEED_NORMALISER = 257


# Define the Pulse Width Modulation (PWM) pins
# rotors
R_B = None
R_A = None
L_B = None
L_A = None
# buzzer
BZ = None
# ultrasonic
US_TRIG = None
US_ECHO = None
# joystick
EVDEV = None
# display
DISPLAY_I2C = None
DISPLAY = None


def wait(time: int = 1):
    """
    Wait for a given amount of time.
    
    Parameters
    ----------
    time : int
        The amount of time to wait in seconds.
    """
    time.sleep(time)

def turn_on():
    """
    Initialise the robot rotors
    """
    # Rotors
    R_B = PWM(Pin(11)) # Right Back
    R_A = PWM(Pin(10)) # Right Front
    L_B = PWM(Pin(13)) # Left Front
    L_A = PWM(Pin(12)) # Left Back
    R_B.freq(DEFAULT_ROTOR_FREQ)
    R_A.freq(DEFAULT_ROTOR_FREQ)
    L_B.freq(DEFAULT_ROTOR_FREQ)
    L_A.freq(DEFAULT_ROTOR_FREQ)
    stop()
    # Buzzer
    BZ = PWM(Pin(22))
    BZ.freq(1000)
    BZ.duty_u16(0)
    # Ultrasonic
    US_TRIG = Pin(0, Pin.OUT)
    US_ECHO = Pin(1, Pin.IN)
    # Joystick
    EVDEV = Evdev(handle_joystick)
    # Display
    DISPLAY_I2C = I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
    DISPLAY = SSD1306_I2C(128, 32, i2c)

def turn_off():
    """
    Turn off the robot rotors
    """
    EVDEV.close()
    BZ.duty_u16(0)
    DISPLAY_I2C.deinit()
    stop()
    
def use_joystick():
    """
    Use the joystick to control the robot
    """
    EVDEV.loop()
    
# ROTORS ----------------------------------------------------------------------

def set_rotors(rb: int = 0, ra: int = 0, lb: int = 0, la: int = 0):
    """
    Set the speed of the rotors
    
    Parameters
    ----------
    rb : int
        The speed of the right back rotor
    ra : int
        The speed of the right front rotor
    lb : int
        The speed of the left back rotor
    la : int
        The speed of the left front rotor
    """
    R_B.duty_u16(rb * DEFAULT_ROTOR_SPEED_NORMALISER)
    R_A.duty_u16(ra * DEFAULT_ROTOR_SPEED_NORMALISER)
    L_B.duty_u16(lb * DEFAULT_ROTOR_SPEED_NORMALISER)
    L_A.duty_u16(la * DEFAULT_ROTOR_SPEED_NORMALISER)

def stop():
    """
    Stop all rotors
    """
    set_rotors(0, 0, 0, 0)

def forward(speed: int = 250):
    """
    Move the robot forward
    
    Parameters
    ----------
    speed : int
        The speed to move forward at
    """
    set_rotors(0, speed, speed, 0)

def backwards(speed: int = 100):
    """
    Move the robot backwards
    
    Parameters
    ----------
    speed : int
        The speed to move backwards at
    """
    set_rotors(speed, 0, 0, speed)

def left(speed: int = 150):
    """
    Move the robot left
    
    Parameters
    ----------
    speed : int
        The speed to move left at
    """
    set_rotors(0, speed, 0, speed)

def right(speed: int = 150):
    """
    Move the robot right
    
    Parameters
    ----------
    speed : int
        The speed to move right at
    """
    set_rotors(speed, 0, speed, 0)

def spin_left():
    """
    Spin the robot left
    """
    speed = 250
    set_rotors(0, speed, 0, speed)
    
def spin_right():
    """
    Spin the robot right
    """
    speed = 250
    set_rotors(speed, 0, speed, 0)

def handle_joystick(evdev_type, evdev_code, evdev_value):
    print( "Joystick event code was: " + str(evdev_code))
    print( "Joystick event value was: " + str(evdev_value))

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
    BZ.duty_u16(volume)
    BZ.freq(frequency)
    wait(seconds)
    BZ.duty_u16(0)
    wait(0.05)

def beep():
    """
    Make a beep sound
    """
    sound(1000)

# ULTRASONIC ------------------------------------------------------------------

def object_distance():
    """
    Get the distance from the ultrasonic sensor
    """
    US_TRIG.value(0)
    wait(0.000002)
    US_TRIG.value(1)
    wait(0.000015)
    US_TRIG.value(0)
    t2 = 0
    while not US_ECHO.value():
        t1 = 0
    t1 = 0
    while US_ECHO.value():
        t2 += 1
    wait(0.001)
    return ((t2 - t1)* 2.0192/10)

def distance():
    """
    Get the distance from the ultrasonic sensor
    
    Returns
    -------
    int
        The distance in cm
    """
    num = 0
    ultrasonic = []
    while num < 5:
        distance = object_distance()
        while int(distance) == -1 :
            distance = object_distance()
            return int(999)
        while (int(distance) >= 500 or int(distance) == 0) :
            distance = object_distance()
            return int(999)
        ultrasonic.append(distance)
        num = num + 1
        wait(0.01)
    distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3])/3
    return int(distance)
