import time
from udp_uart import UdpUart
from pico_car import pico_car

time.sleep(1)
Motor = pico_car()
time.sleep(1)
Motor.Car_Stop()

def pause():
    Motor.Car_toggleLed()
    time.sleep(1)
    Motor.Car_toggleLed()

while True:
    pause()

    Motor.Car_grip(200)
    Motor.Car_grip(200)
    Motor.Car_armJointUp(1,200)
    Motor.Car_armLeft(1)

    pause()

    Motor.Car_grip(0)
    Motor.Car_armJointUp(1,0)
    Motor.Car_armLeft(0)

    pause()

    Motor.Car_release(200)
    Motor.Car_armJointDown(1,200)
    Motor.Car_armRight(1)

    pause()

    Motor.Car_release(0)
    Motor.Car_armJointDown(1,0)
    Motor.Car_armRight(0)

    pause()

    Motor.Car_Run(150,150)

    pause()

    Motor.Car_Stop()

    pause()

    Motor.Car_Left(150,150)

    pause()

    Motor.Car_Stop()

    pause()

    Motor.Car_Right(150,150)

    pause()

    Motor.Car_Stop()

    pause()

    Motor.Car_Back(150,150)

    pause()

    Motor.Car_Stop()

    pause()

