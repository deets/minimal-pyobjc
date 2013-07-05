from objc import IBAction, IBOutlet

from Foundation import (
    NSObject,
    NSLog,
    )

from Cocoa import (
    NSColor,
    )

class ApplicationDelegate(NSObject):


    view = IBOutlet("view")
    
    def init(self):
        self = super(ApplicationDelegate, self).init()
        self.colors = [NSColor.blackColor(), NSColor.redColor(), NSColor.greenColor()]
        return self
        

    def applicationDidFinishLaunching_(self, _):
        NSLog("applicationDidFinishLaunching_")
        

    def applicationWillTerminate_(self, sender):
        pass
    

    @IBAction
    def rotateColor_(self, _sender):
        index = [i for i, color in enumerate(self.colors) if color == self.view.color][0]
        self.view.color = self.colors[(index + 1) % len(self.colors)]
        self.view.setNeedsDisplay_(True)
