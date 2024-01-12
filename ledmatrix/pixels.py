import time
from pico_car import ws2812b

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

SMALL_PANEL = 257
LARGE_PANEL = 769

class Pixels:
    def __init__(self, num_leds):
        self.pixels = ws2812b(num_leds, 0)
        self.pixels.brightness( 20 )
        # inits multidimensional array [][] for the cache of zigzag mapped pixels
        # conditional hardcoding alert, there's 2 panels a 16x16 and a 32x24
        self.width=16;
        self.height=16;
        
        if( len( self.pixels.pixels ) == LARGE_PANEL ):
            self.width=32;
            self.height=24;
            
        self.zigzagMappedPixels = [ [0]*self.height for i in range(self.width)]
        
        if( len( self.pixels.pixels ) == LARGE_PANEL ):
            self.calculateZigZagMappedPixels769()
        else:
            self.calculateZigZagMappedPixels256()

    def show( self ):
        self.pixels.show()

    def clear( self ):
        for i in range(len(self.pixels.pixels)):
            self.pixels.pixels[i] = 0

    def fill(self, centerPixel, color):
        centerOfHLineToFill = self.zigzagMappedPixels[centerPixel[0]][centerPixel[1]]
        rawInnerColor = self.pixels.pixels[centerOfHLineToFill]

        # set a color just to get the set_pixel version, then put the original color back
        self.pixels.set_pixel( centerOfHLineToFill, color[0], color[1], color[2] )
        rawNewColor = self.pixels.pixels[centerOfHLineToFill]
        self.pixels.pixels[centerOfHLineToFill] = rawInnerColor
        
        self.fillSemiCircle(centerPixel[0], centerPixel[1], rawInnerColor, rawNewColor, 1)
        self.fillSemiCircle(centerPixel[0], centerPixel[1] - 1, rawInnerColor, rawNewColor, -1)

    def fillSemiCircle(self, x0, y0, rawInnerColor, rawNewColor, step):
        centerOfHLineToFill = self.zigzagMappedPixels[x0][y0]
        
        while( self.pixels.pixels[centerOfHLineToFill] == rawInnerColor ):
            self.fillLine(x0, y0, rawInnerColor, rawNewColor, 1)
            self.fillLine(x0-1, y0, rawInnerColor, rawNewColor, -1)

            y0+=step
            if( y0 < 0 or y0 >= self.height ):
                break;
            
            centerOfHLineToFill = self.zigzagMappedPixels[x0][y0]

    def fillLine(self, x0, y0, rawInnerColor, rawNewColor, step):
        fillThisPixel = self.zigzagMappedPixels[x0][y0]
       
        while( self.pixels.pixels[fillThisPixel] == rawInnerColor ):
            self.pixels.pixels[fillThisPixel] = rawNewColor

            x0+=step
            if( x0 < 0 or x0 >= self.width ):
                break;

            fillThisPixel = self.zigzagMappedPixels[x0][y0]

    def drawCircle(self, centerPixel, r, color):
        self.drawEllipse(centerPixel, r, r, color)

    def drawEllipseSection(self, x, y, x0, y0, color):
        self.setPixel((x0 + x, y0 - y), color);
        self.setPixel((x0 - x, y0 - y), color);
        self.setPixel((x0 + x, y0 + y), color);
        self.setPixel((x0 - x, y0 + y), color);

    def drawEllipse(self, centerPixel, rx, ry, color):
        rxrx2 = rx
        rxrx2 *= rx
        rxrx2 *= 2

        ryry2 = ry
        ryry2 *= ry
        ryry2 *= 2

        x = rx;
        y = 0;

        xchg = 1
        xchg -= rx
        xchg -= rx
        xchg *= ry
        xchg *= ry

        ychg = rx
        ychg *= rx

        err = 0

        stopx = ryry2
        stopx *= rx
        stopy = 0

        while( stopx >= stopy ):
            self.drawEllipseSection(x, y, centerPixel[0], centerPixel[1], color)
            y+=1
            stopy += rxrx2
            err += ychg
            ychg += rxrx2
            if ( (2*err+xchg) > 0 ):
                x-=1
                stopx -= ryry2
                err += xchg
                xchg += ryry2

        x = 0
        y = ry

        xchg = ry
        xchg *= ry

        ychg = 1
        ychg -= ry
        ychg -= ry
        ychg *= rx
        ychg *= rx

        err = 0

        stopx = 0

        stopy = rxrx2
        stopy *= ry

        while( stopx <= stopy ):
            self.drawEllipseSection(x, y, centerPixel[0], centerPixel[1], color)
            x+=1
            stopx += ryry2
            err += xchg
            xchg += ryry2
            if ( (2*err+ychg) > 0 ):
                y-=1
                stopy -= rxrx2
                err += ychg
                ychg += rxrx2

    def drawTriangle( self, p0, p1, p2, color, bold = False ):
        self.drawPolygon( (p0, p1, p2, p0), color, bold);

    def drawRectangle( self, p0, p1, color, bold = False ):
        self.drawLine( (p0[0],p0[1]), (p0[0],p1[1] ), color, bold);
        self.drawLine( (p0[0],p1[1]), (p1[0],p1[1] ), color, bold);
        self.drawLine( (p1[0],p1[1]), (p1[0],p0[1] ), color, bold);
        self.drawLine( (p1[0],p0[1]), (p0[0],p0[1] ), color, bold);

    def drawPolygon( self, points, color, bold = False ):
        lastPoint = None
        for point in points:
            if( lastPoint != None ):
                self.drawLine(lastPoint, point, color, bold)
                
            lastPoint = point

    def drawLine( self, p0, p1, color, bold = False ):
        if( p1[0] < p0[0] or p1[1] < p0[1]):
            p0, p1 = p1, p0
            
        if( bold == True ):
            self.drawLine_all( p0, p1, color )
        else:
            self.drawLine_min( p0, p1, color )
        
    def drawLine_min( self, p0, p1, color ):
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]

        steps = max(dx,dy)
        xinc = dx/float(steps)
        yinc = dy/float(steps)

        x = p0[0]
        y = p0[1]
        for i in range(steps+1):
            self.setPixel((int(x), int(y)), color)
            
            x+=xinc
            y+=yinc

    def drawLine_all( self, p0, p1, color ):
        step_number = int(abs(p0[0]-p1[0]) + abs(p0[1]-p1[1])) #Number of steps
        step_size = 1.0/step_number #Increment size
        t = 0.0 #Step current increment
        for i in range(step_number):
            self.setPixel( (
                int( round( p0[0] * t + p1[0] * (1 - t) ) ),
                int( round( p0[1] * t + p1[1] * (1 - t) ) )
                ), color )
            t+=step_size

    def setPixel( self, pixel, color ):
        self.pixels.set_pixel( self.zigzagMappedPixels[pixel[0]][pixel[1]], color[0], color[1], color[2] )

    def calculateZigZagMappedPixels256( self ):
        for x in range( 16 ):
            for y in range( 16 ):
                linearPixel = (int(abs(y))*16+int(abs(x)))
                zigzagMappedPixel = 0
                
                # the ( 255 - ) flips the display upsize down
                if( int( ( linearPixel / 16 ) % 2 ) == 0):
                    zigzagMappedPixel = 255 - linearPixel;
                else:
                    zigzagMappedPixel = 255 - ( linearPixel + ( 15 - ( int( linearPixel % 16 ) * 2 ) ) )

                self.zigzagMappedPixels[x][y] = zigzagMappedPixel

    def calculateZigZagMappedPixels769( self ):
        for row in range(32):
            for column in range(3):
                for strip in range(8):
                    pixel = (row * 24) + (column*8) + strip
                    if( column == 1 ):
                        zigzagMappedPixel = 511 - ( (row * 8) + strip )
                    else:
                        zigzagMappedPixel = (row * 8) + (column*8*32) + strip

                    if( int( ( pixel / 8 ) % 2 ) == 0):
                        zigzagMappedPixel = zigzagMappedPixel + ( 7 - ( int( zigzagMappedPixel % 8 ) * 2 ) )
                    
                    self.zigzagMappedPixels[31-row][(column*8) + strip] = zigzagMappedPixel

