from tile import Tile


class InvalidMazeChar(Exception):
    pass


class Maze:
    maze = []
    empty_tiles = set()

    player_position = None
    guardian_position = None

    @classmethod
    def read_maze(cls, file):
        row = 0
        column = 0
        print(f"Opening file : {file}")
        with open(file) as reader:
            # print(reader.readlines())
            for line in reader.readlines():
                line_maze = []
                for char in line.strip():
                    if not Tile.isValid(char):
                        raise InvalidMazeChar(f"on ({row, column}) : '{char}'")
                    line_maze.append(char)
                    if Tile.isFloor(char):
                        cls.empty_tiles.add(f"{row},{column}")
                    elif Tile.isPlayer(char):
                        cls.player_position = (row, column)
                    elif Tile.isGuardian(char):
                        cls.guardian_position = (row, column)
                    column += 1
                cls.maze.append(line_maze)
                column = 0
                row += 1
            print(cls.maze)
            print(len(cls.empty_tiles))
            print(f"player_position {cls.player_position}")
            print(f"guardian_position {cls.guardian_position}")
            cls.remove_empty_tiles_around(cls.player_position[0],cls.player_position[1])
            print(len(cls.empty_tiles))
            cls.remove_empty_tiles_around(cls.guardian_position[0],cls.guardian_position[1])
            print(len(cls.empty_tiles))

    @classmethod
    def remove_empty_tiles_around(cls, row, colunm):
        for r in range(row - 1, row + 2):
            for c in range(colunm - 1, colunm + 2):
                cls.empty_tiles.discard(f"{r},{c}")
