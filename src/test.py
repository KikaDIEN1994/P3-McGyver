import os

import pygame

from maze import Maze
from tile import Tile

pygame.init()


class Test():
    file_path = os.path.join(os.path.dirname(__file__), "assets", "level.txt")
    Maze.read_maze(file_path)
    Maze.print()
    print(Maze.random_empty_tile())


class display():

    background_colour = (255, 255, 255)
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Homer Simpson')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


"""
    maze = []
    empty_tiles = set()
    value = []

    @classmethod
    def rand(cls, file):
        print(file)

        #value = random.choice(tuple(cls.empty_tiles)).split(",")
        #print("value")
    """


# print(Maze.random_empty_tile())
