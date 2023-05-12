import random
from pygame import Vector2
import core
from AsteroidPartie.asteroid import Asteroid
from Interface import Etat
from Interface.Etat import afficherDemarrage, afficherJeu, afficherGameOver, afficherMenu


def setup():
    core.WINDOW_SIZE=[1200,800]
    core.fps = 120
    #interface
    core.memory("etat", Etat.Etat.DEMARRAGE)
    core.memory("textureciel",core.Texture("../asset/fciel.jpg",Vector2(0,0),0,(1200,800)))
    #asteroid
    core.memory("MesSteroïdes",[])
    #

#interface




#asteroid
def creationAsteroid(position):
    ast = Asteroid()
    ast.position = Vector2(0,0)
    ast.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("MesSteroïdes").append(ast)



def run():
    core.cleanScreen()


# interface
    if core.memory('etat') == Etat.Etat.DEMARRAGE:
        afficherDemarrage()

    if core.memory('etat') == Etat.Etat.JEU:
        afficherJeu()
        # asteroid
        print(len(core.memory("MesSteroïdes")))

        if len(core.memory("MesSteroïdes")) < 5:
            # if core.getMouseLeftClick():#len(core.memory("MesSteroïdes")) < 4:
            creationAsteroid([600, 400])

        for p in core.memory("MesSteroïdes"):
            p.deplacement()
            p.draw()
            p.mapTP()

    if core.memory('etat') == Etat.Etat.GAMEOVER:
        afficherGameOver()

    if core.memory('etat') == Etat.Etat.MENU:
        afficherMenu()



core.main(setup,run)