from models import _Tile
from models.labyrinth.simplify import *


def resoudre_lab(laby: 'Labyrinth'):
    laby.tile_arrival._solution = 1
    find(laby.tile_arrival)


def find(tile: _Tile):
    choosen = None
    for voisin in tile.voisins:
        if not voisin.path or voisin._solution == -1:
            continue
        if not voisin._solution:
            if choosen is None:
                choosen = voisin
            elif voisin.distance < choosen.distance:
                choosen._solution = -1
                choosen = voisin
    if choosen:
        choosen._solution = 1
        # if not choosen.is_start:
        find(choosen)
