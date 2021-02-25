from tile import Tile


class InvalidMazeChar(Exception):
    pass


class Maze:
    maze = []
    empty_tiles = set()

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
                        print("InValid")
                        raise InvalidMazeChar(f"on ({row, column}) : '{char}'")
                    line_maze.append(char)
                    if Tile.isFloor(char):
                        cls.empty_tiles.add(f"({row},{column})")
                    # print(f"{row},{column}")
                    column += 1
                cls.maze.append(line_maze)
                column = 0
                row += 1
            print(cls.maze)
            print(cls.empty_tiles)
            # print(cls.maze[1][1])
