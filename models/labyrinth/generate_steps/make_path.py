import random

from models import _Tile
from models.labyrinth.simplify import *


def one_shot_the_path(laby: 'Labyrinth'):
    crossroads_list = find_crossroads(laby)
    while crossroads_list:
        crossroad = crossroads_list.pop()
        make_one_step_path(laby, crossroad)


def make_one_step_path(laby: 'Labyrinth', crossroad: (int, int, str)):
    table = laby.table
    tile_l = crossroad[0]
    tile_c = crossroad[1]
    tile_0: _Tile = table[tile_l, tile_c]

    if crossroad[2] == '-':
        tile_1: _Tile = table[tile_l, tile_c - 1]
        tile_2: _Tile = table[tile_l, tile_c + 1]
    else:
        tile_1: _Tile = table[tile_l - 1, tile_c]
        tile_2: _Tile = table[tile_l + 1, tile_c]

    if tile_1.path is not tile_2.path:  # TODO Le graphique ne s'incere pas entre les deux (envoyer une list.copy en return)
        if len(tile_1.path) > len(tile_2.path):
            tile_win = tile_1
            tile_loose = tile_2
        else:
            tile_win = tile_2
            tile_loose = tile_1
        tile_loose.path.add_tile(tile_0)
        tile_win.path.fusion(tile_loose.path)
    elif random.random() > 0.9:
        tile_1.path.add_tile(tile_0)


def find_crossroads(laby: 'Labyrinth') -> list:
    l_ligne = laby.table.shape[0]
    l_colone = laby.table.shape[1]
    pile = []

    for x in range(2, l_ligne - 2, 2):
        for y in range(1, l_colone, 2):
            pile.append((x, y, '|'))

    for x in range(1, l_ligne, 2):
        for y in range(2, l_colone - 2, 2):
            pile.append((x, y, '-'))

    random.shuffle(pile)
    return pile
