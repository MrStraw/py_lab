from models import Path, Tile
from utils import list_of_int

from models.labyrinth.simplify import *


def init_table(laby: 'Labyrinth'):
    width, height = laby.shape

    nb_wall = int(((width - 1) / 2) * ((height - 1) / 2))
    colors = list_of_int(nb_wall)

    table = laby.table
    for y in range(height):
        for x in range(width):
            if x % 2 and y % 2:
                path = Path(colors.pop())
                table[y, x] = Tile((x, y), table, path)
            else:
                table[y, x] = Tile((x, y), table)

    laby.tile_start.make_start_or_arrival('s')
    laby.tile_start.path = table[1, 1].path
    laby.tile_arrival.make_start_or_arrival('a')
    laby.tile_arrival.path = table[height - 2, width - 2].path
