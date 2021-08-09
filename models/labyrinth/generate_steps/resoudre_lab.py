from models import Tile
from models.labyrinth.simplify import *


def resoudre_lab(laby: 'Labyrinth'):
    laby.tile_arrival._solution = True
    laby.lists.solutions.add(laby.tile_arrival)
    find(laby.tile_arrival, laby)


def find(tile: Tile, laby):
    choosen = None

    for voisin in tile.voisins:
        if not voisin.path or voisin._solution is False or voisin.distance is None:
            continue
        if voisin._solution is None:
            if choosen is None:
                choosen = voisin
            elif voisin.distance < choosen.distance:
                choosen._solution = False
                choosen = voisin

    choosen._solution = True
    laby.lists.solutions.add(choosen)

    if choosen is not laby.tile_start:
        find(choosen, laby)
