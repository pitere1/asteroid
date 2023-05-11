from enum import Enum
import pygame
from pygame.rect import Rect
import core


class Etat(Enum):
    DEMARRAGE = 0
    JEU = 1
    GAMEOVER = 2
    MENU = 3
    CREDIT = 4

def afficherDemarrage():

    print("Demarrage")
    core.Draw.rect((255, 20, 255), ((1200 / 2) - 97, (800 / 2) - 50, 200, 100), 8)
    core.Draw.text((255, 20, 255), "PLAY", ((1200 / 2) - 80, (800 / 2) - 50),80)
    core.Draw.text((150, 200, 20), "Ha Stéroïdes", (250, (800 / 4)-100), 200)

    Pos_Souris = pygame.mouse.get_pos()
    Clicable = Rect(((1200 / 2) - 125, (800 / 2) - 50, 200, 100))


    if Clicable.collidepoint(Pos_Souris):
        core.Draw.text((255, 20, 255), "PLAY", ((1200 / 2) - 80, (800 / 2) - 50),80)

        if core.getMouseLeftClick():
            Pos_SourisPlay = core.getMouseLeftClick()

            if Clicable.collidepoint(Pos_SourisPlay):
                core.memory("etat", Etat.JEU)


def afficherMenu():
    print("Menu")

def afficherJeu():
    print("Jeux")

def afficherGameOver():
    print("GameOver")




