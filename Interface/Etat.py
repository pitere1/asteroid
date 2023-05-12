from enum import Enum
import pygame
from pygame import Vector2
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

    if not core.memory("textureciel").ready:
        core.memory("textureciel").load()
    core.memory("textureciel").box = True  # Display box
    core.memory("textureciel").show()


    core.Draw.rect((255, 20, 255), ((1200 / 2) - 97, (800 / 2) - 50, 200, 100), 8)
    core.Draw.text((255, 20, 255), "PLAY", ((1200 / 2) - 80, (800 / 2) - 50),80)
    core.Draw.text((150, 200, 20), "Ha Stéroïdes", (300, (800 / 4)-100), 100)

    Pos_Souris = pygame.mouse.get_pos()
    Clicable = Rect(((1200 / 2) - 125, (800 / 2) - 50, 200, 100))


    if Clicable.collidepoint(Pos_Souris):
        core.Draw.text((255, 20, 20), "PLAY", ((1200 / 2) - 80, (800 / 2) - 50),80)

        if core.getMouseLeftClick():
            Pos_SourisPlay = core.getMouseLeftClick()

            if Clicable.collidepoint(Pos_SourisPlay):
                core.memory("etat", Etat.JEU)


def afficherMenu():
    print("Menu")

def afficherJeu():
    print("Jeux")

    if not core.memory("textureciel").ready:
        core.memory("textureciel").load()
    core.memory("textureciel").box = True  # Display box
    core.memory("textureciel").show()


def afficherGameOver():
    print("GameOver")

    if not core.memory("textureexpl").ready:
        core.memory("textureexpl").load()
    core.memory("textureexpl").box = True  # Display box
    core.memory("textureexpl").show()

    core.Draw.text((100, 5, 0), "GAME OVER", ((1200 / 2) - 80, (800 / 8) - 50), 80)

    core.Draw.rect((100, 5, 0), ((1200 / 2) - 97, (800 / 2) - 50, 330, 100), 8)
    core.Draw.text((100, 5, 0), "RESTART", ((1200 / 2) - 80, (800 / 2) - 50),80)

    core.Draw.rect((100, 5, 0), ((1200 / 2) - 97, (800 / 4) - 50, 330, 75), 8)
    core.Draw.text((100, 5, 0), "DEMARRAGE", ((1200 / 2) - 80, (800 / 4) - 50), 55)


    Pos_Sourisgo = pygame.mouse.get_pos()
    Clicablerestart = Rect(((1200 / 2) - 97, (800 / 2) - 50, 330, 100))
    Clicabledemarrage = Rect(((1200 / 2) - 97, (800 / 4) - 50, 330, 75))



    if Clicablerestart.collidepoint(Pos_Sourisgo):
        core.Draw.text((200, 10, 0), "RESTART", ((1200 / 2) - 80, (800 / 2) - 50),80)

        if core.getMouseLeftClick():
            Pos_Sourisgo = core.getMouseLeftClick()

            if Clicablerestart.collidepoint(Pos_Sourisgo):
                core.memory("etat", Etat.JEU)



    if Clicabledemarrage.collidepoint(Pos_Sourisgo):
        core.Draw.text((200, 10, 0), "DEMARRAGE", ((1200 / 2) - 80, (800 / 4) - 50), 55)

        if core.getMouseLeftClick():
            Pos_Sourisgo = core.getMouseLeftClick()

            if Clicabledemarrage.collidepoint(Pos_Sourisgo):
                core.memory("etat", Etat.DEMARRAGE)



