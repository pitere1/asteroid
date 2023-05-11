import random
import time

from pygame import Vector2

import core
from AsteroidPartie.asteroid import Asteroid


def setup():
    core.WINDOW_SIZE=[800,800]
    core.fps = 120
    core.memory("mesProjectiles",[])



def creationAsteroid(position):
    ast = Asteroid()
    ast.position = Vector2(position)
    ast.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("mesProjectiles").append(ast)

def run():
    core.cleanScreen()
    if core.getMouseLeftClick():
        if len (core.memory("mesProjectiles"))> 0:
            if time.time() - core.memory("mesProjectiles")[-1].startTime > 0.2 :
                creationProjectile(core.getMouseLeftClick())

        else:
            creationProjectile(core.getMouseLeftClick())

    for p in core.memory("mesProjectiles"):
        if time.time() - p.startTime > p.durreeDeVie :
            core.memory("mesProjectiles").remove(p)

    for p in core.memory("mesProjectiles"):
        p.deplacement()
        p.draw()




core.main(setup,run)