from models import Tile
from models.labyrinth.simplify import *


def resoudre_lab1(laby: 'Labyrinth'):
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


def resoudre_lab(laby: 'Labyrinth'):
    actual_distance = len(laby.lists.distances)
    laby.lists.solutions.add(laby.tile_arrival)
    laby.lists.solutions.add(laby.tile_start)
    while True:
        actual_tiles = laby.lists.distances[actual_distance]
        voisin_actual_tiles: set['Tile'] = set()
        for tile in actual_tiles:
            voisin_actual_tiles |= tile.voisins
        next_tiles = laby.lists.distances[actual_distance - 1]
        tiles_solution = (voisin_actual_tiles & next_tiles)  # .pop()  # TODO pourquoi pas toutes les prendre ?
        laby.lists.solutions |= tiles_solution
        voisins: set['Tile'] = set()
        for tile in tiles_solution:
            for voisin in tile.voisins:
                voisins.add(voisin)
        if laby.tile_arrival in voisins:
            break
        # if laby.tile_arrival in tiles_solution.voisins:
        #     break
        actual_distance -= 1

