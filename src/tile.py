# import pygame


class Tile:
    FLOOR = " "
    WALL = "#"
    PLAYER = "X"
    GUARDIAN = "G"

    ITEM_0 = "0"
    ITEM_1 = "1"
    ITEM_2 = "2"

    asset_of_tile = {
        FLOOR: "floor.png",
        WALL: "wall.png",
        PLAYER: "player.jpg",
        GUARDIAN: "guardian.png",

        ITEM_0: "item_0.png",
        ITEM_1: "item_1.jpg",
        ITEM_2: "item_2.jpg",
    }

    # walls = pygame.image.load("assets/img/wall.png")

    # floors = pygame.image.load("assets/img/floor.png")

    # players = pygame.image.load("assets/img/player.jpg")
    # guardians = pygame.image.load(
    #     "assets/img/guardian.png")
    # syringe = pygame.image.load(
    #     "assets/img/item_1.jpg")
    # needle = pygame.image.load(
    #     "assets/img/item_2.jpg")
    # ether = pygame.image.load(
    #     "assets/img/item_3.png")

    # FILE = open("level.txt", "r")

    # s = FILE.read()

    # print(s)

    # print(FILE)

    ITEMS = [ITEM_0, ITEM_1, ITEM_2]

    VALID_TILES_CHARS = [FLOOR, WALL, PLAYER, GUARDIAN] + ITEMS

    # SPRITE_ITEMS = [syringe, needle, ether]

    # SPRITE = [floors, walls, players, guardians] + SPRITE_ITEMS

    @classmethod
    def is_valid(cls, char):
        return char in cls.VALID_TILES_CHARS

    @classmethod
    def is_floor(cls, char):
        return char == cls.FLOOR

    @classmethod
    def is_wall(cls, char):
        return char == cls.WALL

    @classmethod
    def is_player(cls, char):
        return char == cls.PLAYER

    @classmethod
    def is_guardian(cls, char):
        return char == cls.GUADIAN

    @classmethod
    def is_item(cls, char):
        return char in cls.ITEMS
