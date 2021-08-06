from models import Tile
from models.labyrinth.simplify import *


def impasses(laby: 'Labyrinth'):
    return

    def is_full_path(tile: Tile) -> bool:
        is_path = bool(tile.path)
        is_deadlock = tile in laby.lists.deadlocks
        return is_path and not is_deadlock

    stop = 0
    while stop != 2:
        stop += 1
        for tile in laby.tiles:
            if not is_full_path(tile):
                continue
            if tile is laby.tile_start or tile is laby.tile_arrival:
                continue
            nb_voisin = 0
            for voisin in tile.voisins:
                if is_full_path(voisin):
                    nb_voisin += 1
            if nb_voisin <= 1:
                laby.lists._deadlocks.append(tile)
                stop = 0
