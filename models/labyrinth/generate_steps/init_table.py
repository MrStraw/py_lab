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
                table[y, x] = Tile((x, y), laby, path)
            else:
                table[y, x] = Tile((x, y), laby)
