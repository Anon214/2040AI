from tkinter import *
import Colors as c

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.build_gui()

        self.mainloop()

    def build_gui(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR, width=600, height=600)
        background.grid()

Game()

