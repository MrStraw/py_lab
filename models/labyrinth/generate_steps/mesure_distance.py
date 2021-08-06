from models.labyrinth.simplify import *


def mesure_distance(laby: 'Labyrinth'):
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
