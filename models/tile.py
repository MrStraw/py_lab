from typing import List

import numpy as np

from models.path import Path


class Tile:

    def __init__(self,
                 location: (int, int),
                 table: np.ndarray,
                 path: Path = None,
                 start_or_arrival: str = None,
                 ):

        self.__location: (int, int) = location
        if path:
            path.add_tile(self)
        self._path: Path = path
        self.__is_start_or_arrival: int = 0
        self.make_start_or_arrival(start_or_arrival)
        self._solution: int = 0
        self.distance: int = 0
        self.__table: np.ndarray = table

    @property
    def location(self):
        return self.__location

    @property
    def x(self):
        return self.__location[0]

    @property
    def y(self):
        return self.__location[1]

    @property
    def is_start(self):
        return True if self.__is_start_or_arrival == 1 else False

    @property
    def is_arrival(self):
        return True if self.__is_start_or_arrival == 2 else False

    def make_start_or_arrival(self, value: str):
        if value == 's':
            self.__is_start_or_arrival = 1
        elif value == 'a':
            self.__is_start_or_arrival = 2
        else:
            self.__is_start_or_arrival = 0

    @property
    def is_solution(self):
        return True if self._solution == 1 else False

    @property
    def table(self):
        return self.__table

    @property
    def voisins(self) -> List['Tile']:
        tuples = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        voisins = []
        for t in tuples:
            try:
                voisin: Tile = self.table[t[0] + self.y, t[1] + self.x]
            except IndexError:
                continue
            if not self.x - 1 <= voisin.x <= self.x + 1 or not self.y - 1 <= voisin.y <= self.y + 1:
                continue
            voisins.append(voisin)
        return voisins

    @property
    def color(self) -> int:
        return self._path.color if self._path else 0

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value: Path):
        value.add_tile(self)
        self._path: Path = value

    @path.deleter
    def path(self):
        path = self._path
        for tile in path.tiles:
            tile._path = None
        del path
