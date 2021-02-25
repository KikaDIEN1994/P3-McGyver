import random

from constants import *

class Maze:
#init
    def __init__(self, file):
        self.file = file
        self.grid = []
        self.free_cells = {}

        read_maze(file)

#generate list of lists

    def read_maze(self, file):
        print("read maze", file)

    """
    def generate(file):
        frame = []
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip()
                frame.append(list(line))
        self.grid = frame
        return a
    """

    def display(self, window):
        num_line = 0
        for line in self.grid:
            num_sprite = 0
            for sprite in line:
                X = num_sprite * SPRITE_SIZE
                Y = num_line * SPRITE_SIZE
                if sprite == "#":
                    window.blit(WALL, (X + 30, Y + 30))
                if sprite == "G":
                    window.blit(GUARDIAN, (X + 30, Y + 30))
                num_sprite += 1
            num_line += 1
            return labyrinth

a = generate('./img/level.txt')

print(labyrinth)

"""
W = {
    string: "#",
    description: "Wall"
}
E = " " , empty
P = "X"
O = "O"


"""
"""
 - propriété maze qui contient un array [[W, P, ....], [W, 0, ]]
 - read_maze -> remplir maze
 - objet: faire de regle pour les placer:
    - les placer sur une case vide (E)
    - en placer 3 (aiguille, ether, tube)
    - ne pas placer voisin au gardien
    - ne pas les placer pres du joueur
 - fonction place_objects
    - list_empty = ["1,2","1,3", ... , "13,13"]
"""

"""
    --- 
    -X-      
    ---

"""