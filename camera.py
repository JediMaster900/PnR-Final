import picamera
from picamera import PiCamera
import time

class Cameraphoto(picamera.PiCamera):

    def __init__(self):
        PiCamera.__init__(self)
        self.menu()

    def menu(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {"a": ("Activate Face/Item recognition", self.face),
                "t": ("Take Picture", self.takepic),
                "d": ("Dance", self.dance),
                "c": ("Calibrate", self.calibrate),
                "o": ("Turn test", self.turn_test),
                "s": ("Check status", self.status),
                "f": ("Look forward", self.look_fwd),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = raw_input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    def takepic(self):
        with picamera.PiCamera() as camera:
            camera.rotation = 90
            camera.resolution = (1024, 768)
            camera.start_preview()
            # Camera warm-up time
            time.sleep(2)
            camera.capture('pic.jpg')


try:
    c = Cameraphoto()
except (KeyboardInterrupt, SystemExit):
    from gopigo import *
    stop()
