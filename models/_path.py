class _Path:

    def __init__(self,
                 color: int
                 ):

        self.color = color
        self.__tiles = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def __bool__(self):
        return True

    def add_tile(self, tile):
        self.__tiles.append(tile)
        self.__length += 1
        tile._Case__path = self

    @property
    def tiles(self):
        return self.__tiles

    def fusion(self, other):
        for tile in other.tiles:
            tile.path = self
            self.__tiles.append(tile)
        self.__length += other.__length
        del other
