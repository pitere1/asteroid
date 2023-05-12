import random

from pygame import Vector2

import core
from asteroid.Etat import Etat
from asteroid.asteroid import Asteroid
from asteroid.projectiles import Projectile
from asteroid.vaisseau import Vaisseau


class Map:
    def __init__(self):

        self.projectile = Projectile()
        self.vaisseau = Vaisseau()
        self.etat = Etat()
        self.asteroid = Asteroid()


#vaisseau
def creationVaisseau():
    vais = Vaisseau()
    core.memory("Mesvaisseau").append(vais)



#asteroid
def creationAsteroid(position):
    ast = Asteroid()
    ast.position = Vector2(0,0)
    ast.acceleration = Vector2(core.random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("MesSteroïdes").append(ast)


#projectile
def creationProjectile(position):
    proj = Projectile()
    proj.position = Vector2(position)
    proj.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("mesProjectiles").append(proj)