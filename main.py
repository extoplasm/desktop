import tkinter as tk
import random as rand

class cube():
    def __init__(self):
        self.window = tk.Tk()

        # load animations
        self.idle = [tk.PhotoImage(file='idle.gif', format='gif -index %i' % (i)) for i in range(10)]
        self.sleep = [tk.PhotoImage(file='sleep.gif', format='gif -index %i' % (i)) for i in range(5)]
        self.walkL = [tk.PhotoImage(file='walkL.gif', format='gif -index %i' % (i)) for i in range(8)]
        self.walkR = [tk.PhotoImage(file='walkR.gif', format='gif -index %i' % (i)) for i in range(8)]

        self.frameI = 0
        # init the image
        self.img = self.idle[self.frameI]

        # init window
        self.window.wm_attributes('-transparentcolor', 'white')
        self.window.overrideredirect(True)
        self.window.config(background='white')
        self.window.attributes('-topmost', True)
        self.label = tk.Label(self.window, bd=0, bg='white')

        # event
        self.idleE = [1, 2, 3]
        self.sleepE = [4, 5, 6]
        self.walkLE = [6, 7, 8]
        self.walkRE = [9, 10, 11]
        self.event = rand.randrange(1, 12)

        # start points
        self.x = 1040
        self.y = 550
        self.window.geometry('100x100+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        # idle
        if self.event in self.idleE:
            if self.frameI < len(self.idle):
                self.img = self.idle[self.frameI] # set frame to next frame
                self.frameI += 1 
            else:
                self.frameI = 0 # reset frame
                self.event = rand.randrange(1, 12) 
        # sleep
        elif self.event in self.sleepE:
            if self.frameI < len(self.sleep):
                self.img = self.sleep[self.frameI]
                self.frameI += 1
            else:
                self.frameI = 0
                self.event = rand.randrange(1, 12)
        # walk left
        elif self.event in self.walkLE:
            if self.frameI < len(self.walkL):
                self.img = self.walkL[self.frameI]
                self.frameI += 1
                self.x -= 3
            else:
                self.frameI = 0
                self.event = rand.randrange(1, 12)
        # walk right
        else:
            if self.frameI < len(self.walkR):
                self.img = self.walkR[self.frameI]
                self.frameI += 1
                self.x += 3
            else:
                self.frameI = 0
                self.event = rand.randrange(1, 12)
        # stop cube from going off screen (need to check if this works)
        if self.x > 1100:
            self.x = 0
        if self.x < 0:
            self.x = 1100
        # update frame
        self.window.geometry('100x100+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(300, self.update)
        self.window.lift()
cube()
