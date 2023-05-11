import core
from Interface import Etat
from Interface.Etat import afficherDemarrage, afficherJeu, afficherGameOver, afficherMenu


def setup():
    core.WINDOW_SIZE=[1200,800]
    core.fps = 120
    core.memory("etat", Etat.Etat.DEMARRAGE)


def run():
    core.cleanScreen()

    if core.memory('etat') == Etat.Etat.DEMARRAGE:
        afficherDemarrage()

    if core.memory('etat') == Etat.Etat.JEU:
        afficherJeu()

    if core.memory('etat') == Etat.Etat.GAMEOVER:
        afficherGameOver()

    if core.memory('etat') == Etat.Etat.MENU:
        afficherMenu()


core.main(setup,run)