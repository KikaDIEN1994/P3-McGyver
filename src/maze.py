from tile import Tile


class InvalidMazeChar(Exception):
    pass


class Maze:
    maze = []

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
                    # TODO: verifier que char est bien un tuile valide
                    # créer une classe Tile
                    # Si char n'est pas une Tile valide, envoyer une exception
                    line_maze.append(char)
                    # print(f"{row},{column}")
                    column += 1
                cls.maze.append(line_maze)
                column = 0
                row += 1
            print(cls.maze)
            # print(cls.maze[1][1])
