import core
from Vaisseau.vaisseau import Vaisseau


def setup():
    core.WINDOW_SIZE = [1200, 800]
    core.fps = 120
    core.memory('vaisseau', Vaisseau())







def run():
    core.cleanScreen()
    core.memory('vaisseau').draw()
    core.memory('deplacemnt')


core.main(setup, run)
