class Tile:
    FLOOR = " "
    WALL = "#"
    PLAYER = "X"
    GUADIAN = "G"

    VALID_TILES_CHARS = [FLOOR, WALL, PLAYER, GUADIAN]

    @classmethod
    def isValid(cls, char):
        return char in cls.VALID_TILES_CHARS

    @classmethod
    def isFloor(cls, char):
        return char == cls.FLOOR
