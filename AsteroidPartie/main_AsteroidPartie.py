import core


from AsteroidPartie.asteroid import Asteroid


def setup():
    core.WINDOW_SIZE=[1200,800]
    core.fps = 120
    core.memory("monater",Asteroid())


def run():
    core.cleanScreen()





core.main(setup,run)