import random

from pygame import Vector2
import core


class Asteroid:
    def __init__(self):
        self.taille=47
        self.vel= Vector2(random.uniform(-2,2),random.uniform(-2,2))
        self.acc=Vector2()
        self.position=Vector2()
        self.texture=core.Texture("./pngwing.png",Vector2(self.position))


    def deplacement(self):
        self.position+=self.vel

    def collision(self):
        pass

    def draw(self):

        #core.Draw.circle((255,255,255),self.position,self.taille)
        self.texture.pos=Vector2(self.position.x-50,self.position.y-50)

        if not self.texture.ready:
            self.texture.load()

        self.texture.show()



    def mapTP(self):
        if self.position.x > 1200:
            self.position.x = 0
        if self.position.y > 800:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = 1200
        if self.position.y < 0:
            self.position.y = 800
