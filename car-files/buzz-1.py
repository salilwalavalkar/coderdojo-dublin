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
    BZ.duty_u16(500)
    BZ.freq(587) #D
    time.sleep(0.15) 
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(932) #Bf
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(783) #G
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(783) #G
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(587) #D
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(587) #D
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(880) #A
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(698) #F
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(698) #F
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(587) #D
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(587) #D
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(880) #A
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(698) #F
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(698) #F
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(523) #C
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(523) #C
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(659) #E
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(659) #E
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(698) #F
    time.sleep(0.15)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

    BZ.duty_u16(500)
    BZ.freq(698) #F
    time.sleep(0.05)
    
    BZ.duty_u16(0)
    time.sleep(0.05) #0

