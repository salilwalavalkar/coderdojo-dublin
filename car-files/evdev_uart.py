from machine import Pin, UART, I2C, PWM, Timer

evdevBuffer = [0,0,0,0,0]
    
UART_161 = 0;
UART_196 = 1;
UART_T0 = 2;
UART_C1 = 3;
UART_C0 = 4;
UART_V1 = 5;
UART_V0 = 6;
UART_0 = 7;
UART_STATE = UART_161

class Evdev:

    def __init__(self, callback):
        print("Evdev initialising");
        self.callback = callback
        
        # dont know why but the below duplicate init for uart was required when running autmatically from main.py at device start up
        # if either are not there then there's no uart
        # either line or both works fine when invoking main.py directly from thonny
        # highly likely something else is the issue & below duplication is an accidental, unintentional workaround
        
        self.uart = UART(1, 115200)
        self.uart = UART(1, 115200, tx=Pin(17), rx=Pin(16))
        
        print(self.uart)

	# threading was unreliable when running off macs
	# the macs probably had nothing to do with it
	# call evdev.loop() from main
        #_thread.start_new_thread(self.loop, ())

    def extractEvdev(self, rcv):
        evdev_type = rcv[0]
        evdev_code = (rcv[1]<<8)+rcv[2]
        evdev_value = (rcv[3]<<8)+rcv[4]
        
        return evdev_type, evdev_code, evdev_value

    def loop(self):
        global UART_STATE
        if self.uart.any():
            b = self.uart.read(1)[0]
            
            if( UART_STATE == UART_161 ):
                if( b == 161 ):
                    UART_STATE = UART_196
                
            elif( UART_STATE == UART_196 ):
                if( b == 196 ):
                    UART_STATE = UART_T0
                else:
                    UART_STATE = UART_161
                
            elif( UART_STATE == UART_T0 ):
                evdevBuffer[0] = b
                UART_STATE = UART_C1
                
            elif( UART_STATE == UART_C1 ):
                evdevBuffer[1] = b
                UART_STATE = UART_C0
                
            elif( UART_STATE == UART_C0 ):
                evdevBuffer[2] = b
                UART_STATE = UART_V1
                
            elif( UART_STATE == UART_V1 ):
                evdevBuffer[3] = b
                UART_STATE = UART_V0
                
            elif( UART_STATE == UART_V0 ):
                evdevBuffer[4] = b
                UART_STATE = UART_0
                
            elif( UART_STATE == UART_0 ):
                UART_STATE = UART_161

                if( b == 0 ):
                    evdev_type, evdev_code, evdev_value = self.extractEvdev(evdevBuffer)
                    self.callback(evdev_type, evdev_code, evdev_value)
