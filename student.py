import pigo
import time
import random

'''
MR. A's Final Project Student Helper
'''

class GoPiggy(pigo.Pigo):

    ########################
    ### CONTSTRUCTOR - this special method auto-runs when we instantiate a class
    #### (your constructor lasted about 9 months)
    ########################

    def __init__(self):
        print("Your piggy has be instantiated!")
        # Our servo turns the sensor. What angle of the servo( ) method sets it straight?
        self.MIDPOINT = 90
        # YOU DECIDE: How close can an object get (cm) before we have to stop?
        self.STOP_DIST = 30
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.LEFT_SPEED = 140
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.RIGHT_SPEED = 140
        # This one isn't capitalized because it changes during runtime, the others don't
        self.turn_track = 0
        # Our scan list! The index will be the degree and it will store distance
        self.scan = [None] * 180
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()


    ########################
    ### CLASS METHODS - these are the actions that your object can run
    #### (they can take parameters can return stuff to you, too)
    #### (they all take self as a param because they're not static methods)
    ########################


    ##### DISPLAY THE MENU, CALL METHODS BASED ON RESPONSE
    def menu(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {"n": ("Navigate forward", self.nav),
                "d": ("Dance", self.dance),
                "c": ("Calibrate", self.calibrate),
                "t": ("Turn test", self.turn_test),
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

    def look_fwd(self):
        print('Looking forward...')
        self.servo(self.MIDPOINT)

    def sweep(self):
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
            self.servo(x)
            self.scan[x] = self.dist()
        print("Here's what i saw: ")
        print(self.scan)
        print("Here's how I usually print this:")
        for x in self.scan:
            print(x)

    def safety_dance(self):
        for y in range(3):
            for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
                self.servo(x)
                if self.dist() < 30:
                    print("AAAHHHHH")
                    return
            self.encR(7)
        self.dance()

    def turn_test(self):
        while True:
            ans = raw_input('Turn right, left or stop? (r/l/s): ')
            if ans == 'r':
                val = int(raw_input('/nBy how much?: '))
                self.encR(val)
            elif ans == 'l':
                val = int(raw_input('/nBy how much?: '))
                self.encL(val)
            else:
                break
        self.restore_heading()

    def restore_heading(self):
        print("Now I'll turn back to the starting position.")
        self.set_speed(90, 90)
        if self.turn_track > 0:
            self.encL(abs(self.turn_track))
        elif self.turn_track < 0:

            self.encR(abs(self.turn_track))
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)

    #YOU DECIDE: How does your GoPiggy dance?
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        # self.shimmy()
        self.chicken()
        # self.chacha()
        # self.sprinkler()
        # self.back_it_up()

    def shimmy(self):
        print('shimmy')
        for x in range(3):
            self.servo(30)
            self.encR(3)
            self.servo(140)
            self.encL(3)

    def chicken(self):
        print('chicken')
        for x in range(3):
            self.servo(50)
            self.servo(120)
            if x == 2:
                self.servo(50)
                time.sleep(.2)
        for x in range(3):
            self.servo(120)
            self.servo(50)
            if x == 2:
                self.servo(120)
                time.sleep(.2)
        for x in range(3):
            self.servo(50)
            self.servo(120)
            if x == 2:
                self.servo(50)
                time.sleep(.2)
        for x in range(4):
            self.encF(2)
            time.sleep(.001)





    ########################
    ### MAIN LOGIC LOOP - the core algorithm of my navigation
    ### (kind of a big deal)
    ########################

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("[ Press CTRL + C to stop me, then run stop.py ]\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        # this is the loop part of the "main logic loop"


    def encR(self, enc):
        pigo.Pigo.encR(self, enc)
        self.turn_track += enc

    def encL(self, enc):
        pigo.Pigo.encL(self, enc)
        self.turn_track -= enc


####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit

##################################################################
######## The app starts right here when we instantiate our GoPiggy

g = GoPiggy()
