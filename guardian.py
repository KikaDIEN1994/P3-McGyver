import pygame

class Guardian:

    def __init__(self):

        self.image = pygame.image.load('ressource/Gardien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 460
        self.rect.y = 52