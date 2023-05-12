import random

from pygame import Vector2

import core
from Vaisseau.vaisseau import Vaisseau


def setup():
    core.WINDOW_SIZE = [1200, 800]
    core.fps = 120
    core.memory("Mesvaisseau",[])


def creationVaisseau():
    vais = Vaisseau()
    vais.position = Vector2(500, 400)
    vais.acceleration = Vector2(0,0)
    vais.speed = Vector2(0,0)
    core.memory("Mesvaisseau").append(vais)




def run():
    core.cleanScreen()

    print(len(core.memory("Mesvaisseau")))

    if len (core.memory("Mesvaisseau"))< 1:
        creationVaisseau()

    for vaiss in core.memory("Mesvaisseau"):
        vaiss.deplacement()
        vaiss.draw()
        vaiss.mapTP()

core.main(setup, run)
