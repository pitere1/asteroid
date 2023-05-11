import time

from pygame import Vector2

import core


class Projectile:
    def __init__(self):
        self.taille=5
        self.vitesse=Vector2()
        self.acceleration=Vector2()
        self.position=Vector2()
        self.durreeDeVie=3
        self.startTime=time.time()

    def deplacement(self):
        self.vitesse+=self.acceleration
        self.position+=self.vitesse

    def collision(self):
        pass

    def draw(self):
        core.Draw.circle((255,255,255),self.position,self.taille)