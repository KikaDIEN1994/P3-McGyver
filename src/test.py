import os
import random

from maze import Maze
from tile import Tile


class Test():
    file_path = os.path.join(os.path.dirname(__file__), "assets", "level.txt")
    Maze.read_maze(file_path)
    Maze.print()
    print(Maze.random_empty_tile())

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

# print(empty_tiles)
