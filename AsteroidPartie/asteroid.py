from pygame import Vector2

import core


class Asteroid:
    def __init__(self):
        self.taille=5
        self.vitesse=Vector2()
        self.acceleration=Vector2()
        self.position=Vector2()


    def deplacement(self):
        self.vitesse+=self.acceleration
        self.position+=self.vitesse

    def collision(self):
        pass

    def draw(self):
        core.Draw.circle((150,100,50),self.position,self.taille)



