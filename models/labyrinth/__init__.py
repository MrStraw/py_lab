import numpy as np
from typing import List

from models import Lists
from models.tile import Tile
from models.labyrinth.generate_steps import all_step
from models.labyrinth.screen import screen_lab


class Labyrinth:

    def __init__(self,
                 shape: (int, int),
                 methode: str = 'hole',
                 break_proba: float = 0.1
                 ):
        """
        Create a maze of at least 5x5 shape, filled or with random holes.

        :param shape: (width x height), 5x5 minimum
        :param methode: 'hole' or 'full'
        :param break_proba: probability that a wall becomes a path, even if it is surrounded by the same path through and through
        """
        if not 0 <= break_proba <= 1:
            raise Exception('Argument break_proba need to be between 0 and 1')
        self.break_proba: float = break_proba
        self.lists = Lists()
        width = shape[0] if shape[0] % 2 else shape[0] + 1
        width = 5 if width < 5 else width
        height = shape[1] if shape[1] % 2 else shape[1] + 1
        height = 5 if height < 5 else height
        self.__shape = (width, height)
        self.methode = methode
        self.table: np.ndarray = np.zeros((self.height, self.width), dtype=Tile)
        self.generate()

    @property
    def shape(self):
        return self.__shape

    @property
    def width(self):
        return self.shape[0]

    @property
    def height(self):
        return self.shape[1]

    @property
    def methode(self):
        return self.__methode

    @methode.setter
    def methode(self, value: str):
        methode = 'hole' if value not in ['hole', 'full'] else value
        self.__methode: str = methode

    @property
    def tiles(self) -> List[Tile]:
        tiles = []
        for lignes in self.table:
            for tile in lignes:
                tiles.append(tile)
        return tiles

    @property
    def tile_start(self) -> Tile:
        return self.table[1, 0]

    @property
    def tile_arrival(self) -> Tile:
        return self.table[self.height - 2, self.width - 1]

    @property
    def path(self):
        return self.tile_start.path if self.tile_start is not None else None

    def generate(self):
        """
        re-generate a maze with the same param
        """
        all_step(self)

    def screen(self, mode='B&W'):
        """
        Print the maze with a lot of beautifuls options
        """
        screen_lab(self, mode)
