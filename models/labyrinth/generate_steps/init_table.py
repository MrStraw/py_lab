from models import _Path, _Tile
from utils import list_of_int


def init_table(labyrinth):
    laby = labyrinth
    width, height = laby.shape

    nb_wall = int(((width - 1) / 2) * ((height - 1) / 2))
    colors = list_of_int(nb_wall)

    table = laby.table
    for y in range(height):
        for x in range(width):
            if x % 2 and y % 2:
                path = _Path(colors.pop())
                table[y, x] = _Tile((x, y), table, path)
            else:
                table[y, x] = _Tile((x, y), table)

    laby.tile_start.make_start_or_arrival('s')
    laby.tile_start.path = table[1, 1].path
    laby.tile_arrival.make_start_or_arrival('a')
    laby.tile_arrival.path = table[height - 2, width - 2].path
