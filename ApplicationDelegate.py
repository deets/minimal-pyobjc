import objc
from objc import IBAction
from Foundation import (
    NSObject,
    NSLog,
    )

class ApplicationDelegate(NSObject):

    def init(self):
        self = super(ApplicationDelegate, self).init()
        return self
        

    def applicationDidFinishLaunching_(self, _):
        NSLog("applicationDidFinishLaunching_")
        

    def applicationWillTerminate_(self, sender):
        pass
    
