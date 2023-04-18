from tkinter import *

from configs import Configs

class Device:

    def __init__(self):

        self.window = Tk()

        self.canvas = Canvas(self.window, bg='black', width=Configs.WIDTH, heigh=Configs.HEIGHT)
        self.canvas.pack()

        self.window.bind("<Up>",        self.moveUp)
        self.window.bind("<Down>",      self.moveDown)
        self.window.bind("<Right>",     self.moveRight)
        self.window.bind("<Left>",      self.moveLeft)
        self.window.bind("<Escape>",    self.escape)

    def set_vel(self, vel):
        self.vel = vel

    def moveUp(self, event):
        print('moveUp')
        if(self.vel[0] != [0,  20]):
            self.vel[0] = [0, -20]

    def moveDown(self, event):
        print('moveDown')
        if(self.vel[0] != [0, -20]):
            self.vel[0] = [0,  20]

    def moveLeft(self, event):
        print('moveLeft')
        if(self.vel[0] != [ 20, 0]):
            self.vel[0] = [-20, 0]

    def moveRight(self, event):
        print('moveRight')
        if(self.vel[0] != [-20, 0]):
            self.vel[0] = [ 20, 0]

    def escape(self, event):
        print('ESC')
        self.window.destroy()