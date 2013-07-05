from Cocoa import (
    NSView,
    NSBezierPath,
    NSColor,
    )


class ApplicationView(NSView):


    def drawRect_(self, rect):
        f = self.frame()
        f.origin.x = f.origin.y = 0.0
        color = NSColor.blackColor()
        color.set()
        NSBezierPath.fillRect_(f)
