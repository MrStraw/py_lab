from typing import Set, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Tile


class Lists:

    def __init__(self):
        self._deadlocks = set()
        self._solutions = set()
        self._distances = set()

    @property
    def deadlocks(self) -> Set['Tile']:
        return self._deadlocks

    @property
    def solutions(self) -> Set['Tile']:
        return self._solutions

    @property
    def distances(self) -> Set['Tile']:
        return self._distances
