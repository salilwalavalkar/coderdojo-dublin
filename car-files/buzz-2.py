#setup stuff, dont need to edit the below
# https://pages.mtu.edu/~suits/notefreqs.html
# https://www.hooktheory.com/theorytab/view/noisestorm/crab-rave#:~:text=Crab%20Rave%20is%20written%20in,half%20step%20higher%20(E).
import time
from machine import Pin, PWM
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

def note(frequency, volume, milliseconds):
        BZ.duty_u16(volume)
        BZ.freq(frequency)
        time.sleep(milliseconds) 
        
        BZ.duty_u16(0)
        time.sleep(0.05)

#more setup stuff, dont need to edit the below
if __name__ == "__main__":
    BZ = PWM(Pin(22))
    BZ.freq(1000)
    BZ.duty_u16(0)
    
    #you can start here!
    note(587, 500, 0.15)
    note(932, 500, 0.15)
    note(783, 500, 0.15)
    note(783, 500, 0.05)
    note(587, 500, 0.15)
    note(587, 500, 0.05)
    note(880, 500, 0.15)
    note(698, 500, 0.15)
    note(698, 500, 0.05)
    note(587, 500, 0.15)
    note(587, 500, 0.05)
    note(880, 500, 0.15)
    note(698, 500, 0.15)
    note(698, 500, 0.05)
    note(523, 500, 0.15)
    note(523, 500, 0.15)
    note(659, 500, 0.15)
    note(659, 500, 0.05)
    note(698, 500, 0.15)
    note(698, 500, 0.05)
