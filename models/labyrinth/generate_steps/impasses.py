from models.labyrinth.simplify import *


def impasses(laby: 'Labyrinth'):

    # First clean, on ajoute les chemins:
    # for tile in laby.tiles:
    #     if tile.path:
    #         tile.deadlock = False

    # nettoyage
    stop = 0
    while stop != 2:
        stop += 1
        for tile in laby.tiles:
            if tile.deadlock:
                continue
            if tile is laby.tile_start or tile is laby.tile_arrival:
                continue
            nb_voisin = 0
            for voisin in tile.voisins:
                if not voisin.deadlock:
                    nb_voisin += 1
            if nb_voisin <= 1:
                tile.deadlock = True
                stop = 0
