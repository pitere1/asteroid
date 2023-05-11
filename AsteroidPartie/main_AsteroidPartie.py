import random
import core
from pygame import Vector2
from AsteroidPartie.asteroid import Asteroid





def setup():
    core.WINDOW_SIZE=[1200,800]
    core.fps = 120
    core.memory("MesSteroïdes",[])


def creationAsteroid(position):
    ast = Asteroid()
    ast.position = Vector2(0,0)
    ast.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("MesSteroïdes").append(ast)



def run():
    core.cleanScreen()
    print(len (core.memory("MesSteroïdes")))

    #if len (core.memory("MesSteroïdes"))< 5:
    if core.getMouseLeftClick():#len(core.memory("MesSteroïdes")) < 4:
        creationAsteroid([600,400])


    for p in core.memory("MesSteroïdes"):
        p.deplacement()
        p.draw()
        p.mapTP()




core.main(setup,run)