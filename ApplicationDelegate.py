from objc import IBAction, IBOutlet

from Foundation import (
    NSObject,
    NSLog,
    NSTimer,
    )

from Cocoa import (
    NSColor,
    )

class ApplicationDelegate(NSObject):

    FRAMERATE = 30.0
    
    view = IBOutlet("view")
    
    def init(self):
        self = super(ApplicationDelegate, self).init()
        self.colors = [NSColor.blackColor(), NSColor.redColor(), NSColor.greenColor()]
        return self
        

    def applicationDidFinishLaunching_(self, _):
        NSLog("applicationDidFinishLaunching_")
        self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            1.0 / self.FRAMERATE,
                    self.view,
                    self.view.animate_,
                    None,
                    True
                    )
        


    def applicationWillTerminate_(self, sender):
        if self.timer:
            self.timer.invalidate()
    

    @IBAction
    def rotateColor_(self, _sender):
        index = [i for i, color in enumerate(self.colors) if color == self.view.color][0]
        self.view.color = self.colors[(index + 1) % len(self.colors)]
        self.view.setNeedsDisplay_(True)



    @property
    def xfac(self):
        return self.view.xfac


    @xfac.setter
    def xfac(self, value):
        self.view.xfac = value

        
    @property
    def yfac(self):
        return self.view.yfac


    @yfac.setter
    def yfac(self, value):
        self.view.yfac = value
