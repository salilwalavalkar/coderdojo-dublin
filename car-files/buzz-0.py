#setup stuff, dont need to edit the below
import time
from machine import Pin, PWM
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

#more setup stuff, dont need to edit the below
if __name__ == "__main__":
    BZ = PWM(Pin(22))
    BZ.freq(1000)
    BZ.duty_u16(0)
    
    #you can start here!
    #while True:
    BZ.duty_u16(7000)#volume
    BZ.freq(587) #note
    time.sleep(0.15) #delay
        
    BZ.duty_u16(0) 
    time.sleep(0.05) 

    BZ.duty_u16(10000)#volume
    BZ.freq(587) #note
    time.sleep(0.15) #delay
        
    BZ.duty_u16(0) #silence
    time.sleep(0.05)

