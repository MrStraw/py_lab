from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Tile


class Lists:

    def __init__(self):
        self.deadlocks: set['Tile'] = set()
        self.solutions: set['Tile'] = set()
        self.distances: dict[int, set['Tile']] = dict()

    def distance_add(self, distance, tile: 'Tile'):
        if distance not in self.distances.keys():
            self.distances.update({distance: set()})
        self.distances[distance].add(tile)
