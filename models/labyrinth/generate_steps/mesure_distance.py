from models.labyrinth.simplify import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Tile


def mesure_distance1(laby: 'Labyrinth'):
    laby.tile_start.distance = 1
    laby.lists.distances.add(laby.tile_start)
    cpt = 0
    while not laby.tile_arrival.distance:
        cpt += 1
        for tile in laby.path.tiles:
            if tile.distance == cpt:
                for voisin in tile.voisins:
                    if not voisin.path or voisin.distance:
                        continue
                    voisin.distance = cpt + 1
                    laby.lists.distances.add(voisin)


def mesure_distance(laby: 'Labyrinth'):
    tiles_not_solved: set['Tile'] = laby.path.tiles.copy()
    actual_distance = 1
    laby.lists.distance_add(actual_distance, laby.tile_start)
    tiles_not_solved.remove(laby.tile_start)
    stop = False
    while not stop:
        for tile in laby.lists.distances[actual_distance]:
            for voisin in tile.voisins:
                if voisin in tiles_not_solved:
                    laby.lists.distance_add(actual_distance + 1, voisin)
                    tiles_not_solved.remove(voisin)
                    if voisin is laby.tile_arrival:
                        stop = True
                        break
        actual_distance += 1

