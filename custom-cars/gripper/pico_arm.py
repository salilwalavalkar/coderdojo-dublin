# arm atmega, 0x06
# 4 = grippers, close < 128 < open
# 3 = bottom joint, up < 128 < down
# 2 = middle joint, up < 128 < down
# 1 = top joint, down < 128 < up

# drive atmega, 0x05
# 0 = emergency stop
# 5 = forward, 0 < 255
# 6 = backward, 0 < 255
# 7 = toggle led
# 8 = spin base counterclockwise, 1 = spin, anything else stop
# 9 = spin base clockwise, 1 = spin, anything else stop
# 10 = turn, left < 128 < right

import machine
import time

class pico_arm:
    i2c = machine.I2C(1,sda=machine.Pin(14), scl=machine.Pin(15), freq=400000)

    def __init__(self):
        self.msg = bytearray(3)
        print('Arm ready')

    #drive atmega on 0x05
    def forward(self, speed):
        self.msg[0] = 0
        self.msg[1] = 5
        self.msg[2] = max( min( speed, 255 ), 0 )
        self.i2c.writeto(0x05, self.msg)

    def backward(self, speed):
        self.msg[0] = 0
        self.msg[1] = 6
        self.msg[2] = max( min( speed, 255 ), 0 )
        self.i2c.writeto(0x05, self.msg)

    def direction(self, angle):
        self.msg[0] = 0
        self.msg[1] = 10
        self.msg[2] = max( min( angle, 255 ), 0 )
        self.i2c.writeto(0x05, self.msg)

    # this is more of an emergency stop, it stops all movement
    # however the current variables for motion stored in the atmega
    # are unchanged, so any action will just revert back to what it
    # was doing before
    # set a speed to 0 in forward & backward to more effectivley stop
    def stop(self):
        self.msg[0] = 0
        self.msg[1] = 0
        self.msg[2] = 0
        self.i2c.writeto(0x05, self.msg)

    def toggleLed(self):
        self.msg[0] = 0
        self.msg[1] = 7
        self.msg[2] = 0
        self.i2c.writeto(0x05, self.msg)

    def baseLeft(self, go):
        self.msg[0] = 0
        self.msg[1] = 8
        self.msg[2] = go
        self.i2c.writeto(0x05, self.msg)

    def baseRight(self, go):
        self.msg[0] = 0
        self.msg[1] = 9
        self.msg[2] = go
        self.i2c.writeto(0x05, self.msg)

    #joints, pincer etc atmega on 0x06

    def joint(self, joint, direction, speed):
        if( joint < 1 or joint > 3 or direction < 0 or direction > 1 ):
             return None
        
        # soldered joint 1 motor backwards at the l293d oops
        if( joint == 1 ):
            direction = 1 - direction;
        
        self.msg[0] = 0
        self.msg[1] = joint
        
        if( direction == 1 ):
            self.msg[2] = 128 - max( min( int( speed/2 ), 128 ), 0 )
        elif( direction == 0 ):
            self.msg[2] = 128 + max( min( int( speed/2 ), 128 ), 0 ) 

        self.i2c.writeto(0x06, self.msg)

    def grip(self, direction, speed):
        if( direction < 0 or direction > 1 ):
             return None
        
        self.msg[0] = 0
        self.msg[1] = 4
        
        if( direction == 1 ):
            self.msg[2] = 128 - max( min( int( speed/2 ), 128 ), 0 )
        elif( direction == 0 ):
            self.msg[2] = 128 + max( min( int( speed/2 ), 128 ), 0 ) 

        self.i2c.writeto(0x06, self.msg)

