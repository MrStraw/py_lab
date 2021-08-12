import numpy as np
from typing import List, Tuple, Union, Literal, Set

from models import Lists
from models.tile import Tile
from models.labyrinth.generate_steps import all_step
from models.labyrinth.screen import screen_lab
from utils import generate_seed


class Labyrinth:

    def __init__(self,
                 shape: Tuple[int, int],
                 methode: Literal['hole', 'full'] = 'hole',
                 complexity: float = 0.1,
                 seed: Union[str, float, str, bytes, bytearray] = None,
                 stop_to_step: Literal['distance', 'deadlock', 'solution'] = 'all',
                 set_start_tile: Tuple[int, int] = None,
                 set_arrival_tile: Tuple[int, int] = None
                 ):
        """
        Create a maze of at least 5x5 shape, filled or with random holes.

        :param shape: (width x height), 5x5 minimum
        :param methode: 'hole' or 'full'
        :param complexity: between 0 and 1. The probability that a wall becomes a path, even if it is surrounded by the same path through and through
        :param seed: Seed of the maze
        :param stop_to_step: 'distance', 'deadlock' or 'solution'. Allow to stop at a specific step.
        """
        if seed is None:
            self.seed = generate_seed()
        else:
            self.seed = seed
        assert 0 <= complexity <= 1, 'Argument break_proba need to be between 0 and 1'
        self.complexity: float = complexity

        self.lists = Lists()
        width = shape[0] if shape[0] % 2 else shape[0] + 1
        width = 5 if width < 5 else width
        height = shape[1] if shape[1] % 2 else shape[1] + 1
        height = 5 if height < 5 else height
        self.__shape: Tuple[int, int] = (width, height)
        self._methode: Literal['hole', 'full'] = methode
        self.table: np.ndarray = np.zeros((self.height, self.width), dtype=Tile)
        self._stop_to_step: str = stop_to_step
        self.__setStartTile: Tuple[int, int] = set_start_tile
        self.__setArrivalTile: Tuple[int, int] = set_arrival_tile
        self._tile_start = None
        self._tile_arrival = None
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
    def tiles(self) -> Set[Tile]:
        tiles = set()
        for lignes in self.table:
            for tile in lignes:
                tiles.add(tile)
        return tiles

    @property
    def tile_start(self) -> Tile:
        return self._tile_start

    @property
    def tile_arrival(self) -> Tile:
        return self._tile_arrival

    @property
    def path(self):
        return self.tile_start.path if self.tile_start is not None else None

    def generate(self):
        """
        re-generate a maze with the same param
        """
        all_step(self)

    def screen(self,
               mode: Literal['B&W', 'deadlocks', 'distance', 'solution'] = 'B&W',
               fullscreen: bool = False,
               display: Literal['spread out', 'square'] = 'spread out'
               ):
        """
        Print the maze with a lot of beautifuls options
        """
        screen_lab(self, mode, fullscreen, display)
