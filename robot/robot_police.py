# Police Robot

# 1. Turn On the Police Lights
# 2. Make a Police Siren Sound

from robot import *

turn_on()

message("Robot Police!!")

#while(RUNNING):
for r in range(0, 10):
    use_joystick()

    # get distance
    value = distance()
    message("Distance: " + str(value) + "cm", row = 2)

    # siren sound and lights
    lights_on(BLUE)
    sound(1000, 800, 0.2)
    lights_on(RED)
    sound(600, 800, 0.2)

lights_off()

# spin the robot
#clear_message()
#message("Spinning...")
#message("...........", row = 2)
#spin()
#wait(2)

clear_message()
message("Shutting Down!!")
wait(2)

turn_off()

