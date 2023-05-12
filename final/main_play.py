import random
import time

from pygame import Vector2
import core
from AsteroidPartie.asteroid import Asteroid
from Interface import Etat
from Interface.Etat import afficherDemarrage, afficherJeu, afficherGameOver, afficherMenu
from Vaisseau.vaisseau import Vaisseau
from projectile.projectiles import Projectile


def setup():
    core.WINDOW_SIZE=[1200,800]
    core.fps = 120
    #interface
    core.memory("etat", Etat.Etat.DEMARRAGE)
    core.memory("textureciel",core.Texture("../asset/fciel.jpg",Vector2(0,0),0,(1200,800)))
    core.memory("textureexpl",core.Texture("../asset/explosion.png",Vector2(0,0),0,(1200,800)))
    #asteroid
    core.memory("MesSteroïdes",[])
    #vaisseau
    core.memory("Mesvaisseau",[])
    #projectile
    core.memory("mesProjectiles",[])




#vaisseau
def creationVaisseau():
    vais = Vaisseau()
    core.memory("Mesvaisseau").append(vais)



#asteroid
def creationAsteroid(position):
    ast = Asteroid()
    ast.position = Vector2(0,0)
    ast.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("MesSteroïdes").append(ast)


#projectile
def creationProjectile(position):
    proj = Projectile()
    proj.position = Vector2(position)
    proj.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory("mesProjectiles").append(proj)




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

        # vaisseau
        if len(core.memory("Mesvaisseau")) < 1:
            creationVaisseau()

        for vaiss in core.memory("Mesvaisseau"):
            vaiss.move()
            vaiss.draw()
            vaiss.mapTP()

        # projectile
        if core.getMouseLeftClick():
            if len(core.memory("mesProjectiles")) > 0:
                if time.time() - core.memory("mesProjectiles")[-1].startTime > 0.5:
                    creationProjectile(core.getMouseLeftClick())

            else:
                creationProjectile(core.getMouseLeftClick())

        for p in core.memory("mesProjectiles"):
            if time.time() - p.startTime > p.durreeDeVie:
                core.memory("mesProjectiles").remove(p)

        for p in core.memory("mesProjectiles"):
            p.deplacement()
            p.draw()

    if core.memory('etat') == Etat.Etat.GAMEOVER:
        afficherGameOver()

    if core.memory('etat') == Etat.Etat.MENU:
        afficherMenu()








core.main(setup,run)