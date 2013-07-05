import time
from math import cos, sin
from Cocoa import (
    NSView,
    NSBezierPath,
    NSColor,
    NSCompositeCopy,
    NSImage,
    )
from Quartz import (
    NSBitmapImageRep,
    NSCalibratedWhiteColorSpace,
)

import numpy

class ApplicationView(NSView):

    
    def initWithFrame_(self, frame):
        self.color = NSColor.blackColor()
        self.pixel_buffer = numpy.zeros((256, 256), numpy.uint8)
        self.blob = numpy.zeros((16, 16), numpy.uint8)
        self.blob += 16
        self.t = .0
        self.now = time.time()
        self.xfac = 3.5
        self.yfac = 2.5
        return super(ApplicationView, self).initWithFrame_(frame)


    def drawRect_(self, rect):
        f = self.frame()
        f.origin.x = f.origin.y = 0.0
        self.color.set()
        NSBezierPath.fillRect_(f)

        img = self.image_from_buffer()
        
        img.drawInRect_fromRect_operation_fraction_(
            f,
            ((0,0), (0, 0)),
            NSCompositeCopy,
            1.0,
            )


    def animate_(self, _timer):
        elapsed = time.time() - self.now
        self.now += elapsed
        self.t += elapsed
        bx = int(cos(self.t * self.xfac) * (128 - 16) + 128)
        by = int(sin(self.t * self.yfac) * (128 - 16) + 128)
        bwidth, bheight = self.blob.shape
        self.pixel_buffer[bx:bx + bwidth, by:by + bheight] += self.blob
        self.setNeedsDisplay_(True)
        

    def image_from_buffer(self):
        buf = buffer(self.pixel_buffer)
        width, height = self.pixel_buffer.shape
        planes = (buf, None, None, None, None)
        brep = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(
            planes,
            width,
            height,
            8,
            1,
            False,
            True,
            NSCalibratedWhiteColorSpace,
            width,
            0
            )

        img = NSImage.alloc().initWithSize_((width, height))
        img.addRepresentation_(brep)
        return img
