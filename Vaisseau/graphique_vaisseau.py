import random
from operator import pos


from pygame import Vector2

import core


class Vaisseau():
    def __init__(self,):
        self.vMax = 10
        self.accMax = 5
        self.acc = Vector2(0, 100)
        self.vitesse = Vector2(0, 100)
        self.position = Vector2(400,400)
        #self.vel = Vector2(random.uniform(-100, 100), random.uniform(-100, 100))
        #self.pos = Vector2(random.randint(400,400), random.randint(400, 400))
        self.texture=core.Texture("./1945907.png", Vector2(650, 400))
        self.position = pos


    def draw(self):

        if not self.texture.ready:
            self.texture.load()
        self.texture.show()



    def move(self):

        if core.getKeyPressList("z"):
            self.texture.pos-=10
        if core.getKeyPressList("s"):
            self.texture.pos+=10
        if core.getKeyPressList("q"):
            self.texture.x-=10
        if core.getKeyPressList("d"):
            self.texture.x+=10




