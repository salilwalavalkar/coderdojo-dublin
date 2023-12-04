# Program: Christmas Special 2023

# 1. Print 'Merry Christmas!!' on screen
# 2. Turn On the green lights
# 3. Turn On the red lights

from robot import *

turn_on()

message('Merry Christmas!!')
wait(2)

lights_on(RED)
wait(1)

lights_on(GREEN)
wait(1)

lights_off()
clear_message()

message('Good Night!!')
wait(1)

turn_off()

