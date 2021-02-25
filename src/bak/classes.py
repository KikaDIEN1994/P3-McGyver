import pygame

from constants import*

class Player:

    #stat of Macgyver
    def __init__(self):

        self.health = 1
        self.speed = 55
        self.image = pygame.image.load("assets/img/MacGyver.png").convert_alpha()
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

class Map():
    """class object Map which define the labyrinth.
    It has one attribut : an empty grid.
    and takes as parameter the file.txt which contains the map.
    This class has two methods: one to generate the structure : a list of list
    and one to display the grid over the pygame window."""

    def __init__(self, file):
        self.file = file
        self.grid = []

    def generate(file):
        """Method which generate the structure from the file.txt"""
        frame = []
        #let generate the list of lists
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip() #be careful to cut the line break
                frame.append(list(line))
        self.grid = frame # we get the list of lists in the attribut

    def display(self, window):
        """from the grid we display each sprite match with a code : 
        "#" for picture of a wall , "G" for the guardian. Each sprite have
        x and y coordinates and a size in pixel."""
        num_line = 0 #we begin with the first list so the fist line
        for line in self.grid:
            num_sprite = 0 #we begin with the first square
            for sprite in line:
                X = num_sprite * SPRITE_SIZE
                Y = num_line * SPRITE_SIZE
                if sprite == "#":
                    window.blit(WALL, (X + 30, Y + 30)) #we load a wall picture over the window 
                if  sprite == "G":                      #we add 30 for the offset of the black outline
                    window.blit(ARRIVAL, (X + 30, Y + 30)) #we load a arrival picture over the window
                num_sprite += 1
            num_line += 1

maze = display('./assets/level.txt')
