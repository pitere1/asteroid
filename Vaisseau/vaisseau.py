import random
from operator import pos

from pygame import Vector2

import core


class Vaisseau:
    def __init__(self):
        self.taille=20
        self.speed=Vector2()
        self.acc=Vector2()
        self.pos=Vector2()
        #self.texture=core.Texture("../asset/pngwing.png",Vector2(self.position))



    def deplacement(self):
        self.speed += self.acc
        self.pos += self.speed

    def move(self):
        if core.getKeyPressList("z"):
                self.acc = self.acc.y-10
        if core.getKeyPressList("s"):
                self.acc = self.acc.y+10
        if core.getKeyPressList("q"):
                self.acc = self.acc.x-10
        if core.getKeyPressList("d"):
                self.acc = self.acc.x+10


    def collision(self):
        pass

    def draw(self):

        core.Draw.circle((255,255,255),self.position,self.taille)


    def mapTP(self):
        if self.pos.x > 1200:
            self.pos.x = 0
        if self.pos.y > 800:
            self.pos.y = 0

        if self.pos.x < 0:
            self.pos.x = 1200
        if self.pos.y < 0:
            self.pos.y = 800







