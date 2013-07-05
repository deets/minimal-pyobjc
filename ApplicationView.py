from Cocoa import (
    NSView,
    NSBezierPath,
    NSColor,
    )


class ApplicationView(NSView):


    def initWithFrame_(self, frame):
        self.color = NSColor.blackColor()
        return super(ApplicationView, self).initWithFrame_(frame)
    

    def drawRect_(self, rect):
        f = self.frame()
        f.origin.x = f.origin.y = 0.0
        self.color.set()
        NSBezierPath.fillRect_(f)
