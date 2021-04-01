class Tile:
    FLOOR = " "
    WALL = "#"
    PLAYER = "X"
    GUADIAN = "G"

    ITEM_0 = "0"
    ITEM_1 = "1"
    ITEM_2 = "2"

    ITEMS = [ITEM_0, ITEM_1, ITEM_2]

    VALID_TILES_CHARS = [FLOOR, WALL, PLAYER, GUADIAN] + ITEMS

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
