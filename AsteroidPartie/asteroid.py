import random

from pygame import Vector2
import core


class Asteroid:
    def __init__(self):
        self.taille=20
        self.vel= Vector2(random.uniform(-2,2),random.uniform(-2,2))
        self.acc=Vector2()
        self.position=Vector2()



    def deplacement(self):
        self.position+=self.vel

    def collision(self):
        pass

    def draw(self):
        core.Draw.circle((255,255,255),self.position,self.taille)

    def mapTP(self):
        if self.position.x > 1200:
            self.position.x = 0
        if self.position.y > 800:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = 1200
        if self.position.y < 0:
            self.position.y = 800
