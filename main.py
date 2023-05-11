import pygame
from pygame.rect import Rect
import core


def setup():
    core.WINDOW_SIZE= [1200,800]
    core.fps=120


def run():
    draw()



def draw():
    core.Draw.rect((255, 20, 255), ((1200 / 2) - 125, (800 / 2) - 50, 200, 100))
    core.Draw.text((255, 20, 255), "PLAY", ((1200 / 2) - 110, (800 / 2) - 50))

    Pos_Souris = pygame.mouse.get_pos()
    Clicable = Rect(((1200 / 2) - 125, (800 / 2) - 50, 200, 100))

    if Clicable.collidepoint(Pos_Souris):

        core.Draw.text((255, 255, 0), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 110, (core.WINDOW_SIZE[1] / 2) - 40), 80,
                       'Doctor Glitch')
        if core.getMouseLeftClick():
            Pos_Souris = core.getMouseLeftClick()



core.main(setup,run)