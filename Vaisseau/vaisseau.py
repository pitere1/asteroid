import random
from operator import pos

from pygame import Vector2

import core


class Vaisseau():
    def __init__(self,):
        self.vMax = 10
        self.accMax = 5
        self.acc = Vector2(0, 100)
        self.speed = Vector2(0, 100)
        #self.position = Vector2(400,400)
        #self.vel = Vector2(random.uniform(-100, 100), random.uniform(-100, 100))
        #self.pos = Vector2(random.randint(0, 800), random.randint(0, 800))
        self.texture=core.Texture("./1945907.png", Vector2(650, 400))
        #self.position = pos
        self.pos = Vector2(0, 0)
        self.vMax= 10
        self.accMax=10

    def draw(self):

        if not self.texture.ready:
            self.texture.load()
        self.texture.show()

    def deplacement(self):
        self.speed += self.acc
        self.pos += self.speed

    def move(self):
        #for self.texture in self.pos:
         #   if core.getKeyPressList("z"):
          #      self.texture = self.pos.y=-10
           # if core.getKeyPressList("s"):
            #    self.texture.pos.y=+10
            #if core.getKeyPressList("q"):
             #   self.texture.pos.x=-10
            #if core.getKeyPressList("d"):
             #   self.texture.pos.x=+10


        i = random.randint(0, 19)
        for j in self.texture.pos :


            if not j.bot:

                if core.getKeyPressList("z"):
                    j.acceleration.y -= 1
                if core.getKeyPressList("s"):
                    j.acceleration.y += 1
                if core.getKeyPressList("q"):
                    j.acceleration.x -= 1
                if core.getKeyPressList("d"):
                    j.acceleration.x += 1
                j.deplacement()






