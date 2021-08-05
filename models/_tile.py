import numpy as np

from models._path import _Path


class _Tile:

    def __init__(self,
                 location: (int, int),
                 table: np.ndarray,
                 path: _Path = None,
                 start_or_arrival: str = None,
                 ):

        self.__location: (int, int) = location
        if path:
            path.add_tile(self)
        self.__path: _Path = path
        self.__is_start_or_arrival: int = 0
        self.make_start_or_arrival(start_or_arrival)
        self._solution: int = -1
        self.distance: int = 0
        self.deadlock: bool = False
        self.__table: np.ndarray = table

    @property
    def location(self):
        return self.__location

    @property
    def x(self):
        return self.location[0]

    @property
    def y(self):
        return self.location[1]

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
    def voisins(self) -> list:
        tuples = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        voisins = []
        for t in tuples:
            try:
                case_voisine: _Tile = self.table[t[0] + self.y, t[1] + self.x]
            except IndexError:
                continue
            voisins.append(case_voisine)
        return voisins

    @property
    def color(self) -> int:
        return self.__path.color if self.__path else 0

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value: _Path):
        value.add_tile(self)
        self.__path = value
