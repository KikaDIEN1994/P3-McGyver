import os

from maze import Maze

print(os.path.dirname(__file__))

file_path = os.path.join(os.path.dirname(__file__), "assets", "level.txt")
# file_path = os.path.join(os.path.dirname(__file__), "assets", "level_invalid.txt")

print(file_path)

Maze.read_maze(file_path)
