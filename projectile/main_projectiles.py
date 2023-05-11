import random
import time
import core
from pygame import Vector2
from projectile.projectiles import Projectile




def setup():
    core.WINDOW_SIZE=[1200,800]
    core.fps = 120
    core.memory("mesProjectiles",[])



def creationProjectile(position):
    proj = Projectile()
    proj.position = Vector2(position)
    proj.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("mesProjectiles").append(proj)

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