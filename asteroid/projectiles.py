import time

from pygame import Vector2

import core


class Projectile:
    def __init__(self):
        self.taille=7
        self.vitesse=Vector2()
        self.acceleration=Vector2()
        self.position=Vector2()
        self.durreeDeVie=2
        self.startTime=time.time()
        #self.texture=core.Texture("../asset/proj.png",Vector2(self.position))

    def deplacement(self):
        self.vitesse+=self.acceleration
        self.position+=self.vitesse

    def collision(self):
        pass

    def draw(self):
        core.Draw.circle((255,10,0),self.position,self.taille)

        #self.texture.pos = Vector2(self.position.x - 50, self.position.y - 50)

        #if not self.texture.ready:
         #   self.texture.load()

        #self.texture.show()