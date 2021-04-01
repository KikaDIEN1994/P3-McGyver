import os

from .maze import Maze


class App:
    def run(self):
        print(os.path.dirname(__file__))

        file_path = os.path.join(os.path.dirname(
            __file__), "assets", "level.txt")
        print(file_path)

        Maze.read_maze(file_path)

        print(Maze.random_empty_tile())
        Maze.print()
