from pygame import Vector2

import core
from Vaisseau.graphique_vaisseau import Vaisseau


def setup():
    core.WINDOW_SIZE = [1500, 800]
    core.fps = 120
    core.memory('vaisseau', Vaisseau())







def run():
    core.cleanScreen()
    core.memory('vaisseau').draw()




core.main(setup, run)