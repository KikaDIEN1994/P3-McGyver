import pygame

from player import Player
from items import Items
from guardian import Guardian

class Game:

    def __init__(self):
        self.player = Player()
        self.items = Items()

