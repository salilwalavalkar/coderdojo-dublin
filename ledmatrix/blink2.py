from time import sleep
from pixels import *

pixels = Pixels(LARGE_PANEL)

def blink( r ):
    pixels.clear()
    drawWhite( 8, r )
    drawWhite( 24, r )
    pixels.show()

def drawWhite( x, r ):
    pixels.drawEllipse((x,8),7,r,WHITE)
    pixels.fill((x,8),WHITE)

def drawEye( x, iris ):
    drawWhite( x, 4 )
    pixels.drawCircle((x+iris,8),2,BLUE)
    pixels.fill((x+iris,8),BLUE)
    if( iris > 0 ):
        pixels.drawRectangle((x+iris,8),(x+iris+1,9),BLACK)
    else:
        pixels.drawRectangle((x+iris-1,8),(x+iris,9),BLACK)

def clearEye( x, iris ):
    if( iris > 0 ):
        pixels.drawRectangle((x+iris,8),(x+iris+1,9),BLUE)
    else:
        pixels.drawRectangle((x+iris-1,8),(x+iris,9),BLUE)
    pixels.fill((x+iris,8),WHITE)

while True:
    for r in range( 1, 5, 1 ):
        blink(r)

    drawEye( 8, 4 )
    drawEye( 24, 4 )
    pixels.show()
    sleep(0.4)

    for iris in range( 4, -5, -1 ):
        pixels.clear()
        drawEye( 8, iris )
        drawEye( 24, iris )
        pixels.show()

    sleep(0.1)

    for iris in range( -4, 5, 1 ):
        pixels.clear()
        drawEye( 8, iris )
        drawEye( 24, iris )
        pixels.show()

    sleep(0.4)
    
    for r in range( 4, 0, -1 ):
        blink(r)
