import random
from operator import pos

from pygame import Vector2

import core
from projectile.projectiles import Projectile


class Vaisseau:
    def __init__(self):
        self.taille=30
        self.speed=Vector2()
        self.acc=Vector2()
        self.pos=Vector2(600, 400 )
        self.vmax=1
        self.accMax=1
        self.dec=0.95
        self.texture=core.Texture("./asset/vaisseau.png",Vector2(self.pos))





    def move(self):
        if core.getKeyPressList("z"):
            self.acc.y -= 1
        if core.getKeyPressList("s"):
            self.acc.y += 1
        if core.getKeyPressList("q"):
            self.acc.x -= 1
        if core.getKeyPressList("d"):
            self.acc.x += 1
        #if core.getKeyPressList("SPACE"):
            #self.speed.scale_to_length(0)
            #self.acc.scale_to_length(0)

        if self.acc.x < 0 :
            self.speed.x *= self.dec
        if self.acc.y < 0:
            self.speed.y *= self.dec




        self.speed += self.acc
        self.pos += self.speed



        if self.acc.length() > self.accMax:
            self.acc.scale_to_length(self.accMax)

        if self.speed.length() > self.vmax:
            self.speed.scale_to_length(self.vmax)

    def collision(self):
        pass

    def draw(self):

        #core.Draw.circle((255,255,255),self.pos,self.taille)
        self.texture.pos = Vector2(self.pos.x - 50, self.pos.y - 50)

        if not self.texture.ready:
            self.texture.load()

        self.texture.show()


    def mapTP(self):
        if self.pos.x > 1200:
            self.pos.x = 0
        if self.pos.y > 800:
            self.pos.y = 0

        if self.pos.x < 0:
            self.pos.x = 1200
        if self.pos.y < 0:
            self.pos.y = 800







