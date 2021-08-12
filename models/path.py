from typing import Set, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Tile


class Path:

    def __init__(self,
                 color: int
                 ):

        self.color: int = color
        self.__tiles = set()
        self.__length: int = 0

    def __len__(self):
        return self.__length

    def __bool__(self):
        return True

    def add_tile(self, tile: 'Tile'):
        self.__tiles.add(tile)
        self.__length += 1
        tile._path = self

    @property
    def tiles(self) -> Set['Tile']:
        return self.__tiles

    def fusion(self, other):
        for tile in other.tiles:
            tile.path = self
        self.__tiles |= other.tiles
        self.__length += other.__length
        del other
