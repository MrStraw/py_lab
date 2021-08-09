from models import Tile, Path
from models.labyrinth.simplify import *


def set_start_and_arrival(laby: 'Labyrinth'):
    if laby._Labyrinth__setStartTile is None:
        laby._Labyrinth__setStartTile = (0, 1)
    if laby._Labyrinth__setArrivalTile is None:
        laby._Labyrinth__setArrivalTile = (laby.width - 1, laby.height - 2)
    if laby._Labyrinth__setStartTile == laby._Labyrinth__setArrivalTile:
        raise Exception("Start tile and arrival tile can't be at the same location")

    div_height = laby.height // 2
    div_width = laby.width // 2
    start = (laby._Labyrinth__setStartTile[0], laby._Labyrinth__setStartTile[1], 'start')
    arrival = (laby._Labyrinth__setArrivalTile[0], laby._Labyrinth__setArrivalTile[1], 'arrival')

    for x, y, where in [start, arrival]:
        if x > laby.width - 2:
            x = laby.width - 2
        if x < 1:
            x = 1
        if y > laby.width - 2:
            y = laby.width - 2
        if y < 1:
            y = 1
        if not x % 2 and not y % 2:
            x = x + 1 if x < div_width else x - 1
            y = y + 1 if y < div_height else y - 1
        tile: Tile = laby.table[y, x]

        if tile.path is None:
            tile.path = Path(-1)
        for voisin in tile.voisins:
            if voisin.path:
                voisin.path.fusion(tile.path)

        if where == 'start':
            tile.make_start_or_arrival('s')
        else:
            tile.make_start_or_arrival('a')
