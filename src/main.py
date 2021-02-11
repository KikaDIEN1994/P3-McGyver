import os

import maze

print(os.path.dirname(__file__))

file_path = os.path.join(os.path.dirname(__file__), "assets", "level.txt")

print(file_path)

maze.read_maze(file_path)
