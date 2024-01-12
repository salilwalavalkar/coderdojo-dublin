from time import sleep
from pixels import *

pixels = Pixels(SMALL_PANEL)

def drawEye( x ):
    pixels.clear()
    pixels.drawEllipse((8,8),7,r,WHITE)
    pixels.fill((8,8),WHITE)
    pixels.drawCircle((x,8),2,BLUE)
    pixels.fill((x,8),BLUE)
    if( x >= 8 ):
        pixels.drawRectangle((x,8),(x+1,9),BLACK)
    else:
        pixels.drawRectangle((x-1,8),(x,9),BLACK)


while True:
    for r in range( 1, 5, 1 ):
        pixels.clear()
        pixels.drawEllipse((8,8),7,r,WHITE)
        pixels.fill((8,8),WHITE)
        pixels.show()
        sleep(0.05)

    drawEye( 12 )
    pixels.show()
    sleep(0.4)

    for x in range( 12, 3, -1 ):
        drawEye( x )
        pixels.show()

    sleep(0.1)

    for x in range( 4, 13, 1 ):
        drawEye( x )
        pixels.show()

    sleep(0.4)
    
    for r in range( 4, 0, -1 ):
        pixels.drawEllipse((8,8),7,r,WHITE)
        pixels.fill((8,8),WHITE)
        pixels.show()
        pixels.clear()
        sleep(0.05)
