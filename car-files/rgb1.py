import time
from pico_car import ws2812b

num_leds = 8  
pixels = ws2812b(num_leds, 0)

#pixel_num, red, green, blue
while True:
    pixels.set_pixel(0, 10, 0, 0)
    pixels.show()
    time.sleep(0.5)

    pixels.set_pixel(0, 10, 10, 0)
    pixels.show()
    time.sleep(0.5)


    pixels.set_pixel(0, 10, 0, 1z0)
    pixels.show()
    time.sleep(0.5)
    
    
    piels.set_pi
