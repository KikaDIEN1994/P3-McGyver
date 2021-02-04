import pygame

class Player:

    #stat of Macgyver
    def __init__(self):

        self.health = 1
        self.speed = 55
        self.image = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 107

    #Function to move player
    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed