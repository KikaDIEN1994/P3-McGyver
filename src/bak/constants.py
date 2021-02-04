import pygame
from pygame.locals import *

"""
This file contain all constant like image of game sprite size and window size
"""

#Setting sprite
NB_SPRITE = 15
SPRITE_SIZE = 30

#Setting window
SCREEN_SIZE = ((NB_SPRITE + 2) * SPRITE_SIZE, (NB_SPRITE + 2) * SPRITE_SIZE)
WINDOW = pygame.display.set_mode(SCREEN_SIZE)

#We load backgroung img
WALL = pygame.image.load("assets/img/wall.png")
BACKGROUND = pygame.image.load("assets/img/background.png").convert_alpha()

#We load exit img
EXIT = pygame.image.load("assets/img/exit.png").convert_alpha()

#We load object img
TUBE = pygame.image.load("assets/img/tube.png").convert_alpha()
NEEDLE = pygame.image.load("assets/img/aiguille.png").convert_alpha()
ETHER = pygame.image.load("assets/img/ether.png").convert_alpha()

#We load characters img
MG = pygame.image.load("assets/img/MacGyver.png").convert_alpha()
GUARDIAN = pygame.image.load("assets/img/Gardien.png").convert_alpha()


GUARDIAN = {
    asset: pygame.image.load("assets/img/Gardien.png").convert_alpha(),
    char: "G"
}