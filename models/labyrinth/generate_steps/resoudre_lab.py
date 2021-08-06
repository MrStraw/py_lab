from models import Tile
from models.labyrinth.simplify import *


def resoudre_lab(laby: 'Labyrinth'):
    laby.tile_arrival._solution = 1
    laby.lists.solutions.add(laby.tile_arrival)
    find(laby.tile_arrival, laby)


def find(tile: Tile, laby):
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
        laby.lists.solutions.add(choosen)
        find(choosen, laby)
