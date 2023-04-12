import time
from pico_car import ws2812b

num_leds = 8  
pixels = ws2812b(num_leds, 0)

while True:
    for pixel in range(num_leds):
        pixels.set_pixel(pixel, , 3, 100)
        pixels.show()
        time.sleep(0.9)

    for pixel in range(num_leds):
        pixels.set_pixel(pixel, 3, 0, 0)
        pixels.show()
        time.sleep(0.9)

    for pixel in range(num_leds):
        pixels.set_pixel(pixel, 0, 0, 3)
        pixels.show()
        time.sleep(0.9)
