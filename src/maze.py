import random

from tile import Tile


class InvalidMazeChar(Exception):
    pass


class Maze:
    NUMBER_OF_ITEMS = 3

    maze = []
    empty_tiles = set()

    player_position = None
    guardian_position = None

    items_0 = 1
    items_1 = 1
    items_2 = 1

    @classmethod
    def read_maze(cls, file):
        row = 0
        column = 0
        with open(file) as reader:
            for line in reader.readlines():
                line_maze = []
                for char in line.strip():
                    if not Tile.is_valid(char):
                        raise InvalidMazeChar(f"on ({row, column}) : '{char}'")
                    line_maze.append(char)
                    if Tile.is_floor(char):
                        cls.empty_tiles.add(f"{row},{column}")
                    elif Tile.is_player(char):
                        cls.player_position = (row, column)
                    elif Tile.is_guardian(char):
                        cls.guardian_position = (row, column)
                    column += 1
                cls.maze.append(line_maze)
                column = 0
                row += 1
            # print(cls.maze)
            print(len(cls.empty_tiles))
            print(f"player_position {cls.player_position}")
            print(f"guardian_position {cls.guardian_position}")
            cls.remove_empty_tiles_around(
                cls.player_position[0], cls.player_position[1])
            print(len(cls.empty_tiles))
            cls.remove_empty_tiles_around(
                cls.guardian_position[0], cls.guardian_position[1])
            print(len(cls.empty_tiles))
            cls.put_items()

    @classmethod
    def remove_empty_tiles_around(cls, row, colunm):
        for r in range(row - 1, row + 2):
            for c in range(colunm - 1, colunm + 2):
                cls.empty_tiles.discard(f"{r},{c}")

    @classmethod
    def print(cls):
        for row in cls.maze:
            print("".join(row))

    @classmethod
    def random_empty_tile(cls):
        return random.choice(tuple(cls.empty_tiles)).split(",")

    @classmethod
    def put_items(cls):
        print(f"put {cls.NUMBER_OF_ITEMS} items")
        for item in Tile.ITEMS:
            print("item : ", item)
            row, column = [int(coord) for coord in cls.random_empty_tile()]
            print(f"row : {row} , column: {column}")
            cls.maze[row][column] = item
            cls.remove_empty_tiles_around(row, column)
