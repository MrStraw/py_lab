import tkinter as tk
from time import sleep

from models import Tile

from models.labyrinth.simplify import *
from utils import int_to_grad_hexa


def print_mode(laby: 'Labyrinth', canvas: tk.Canvas, pixel_len, mode: str = 'B&W'):
    def make_pix(tile: Tile, color: str, outline: str = ''):
        x_pix = tile.x * pixel_len[0]
        y_pix = tile.y * pixel_len[1]
        outline_width = min(pixel_len[0], pixel_len[1]) / 2.4
        tile.print_rectangle = canvas.create_rectangle(x_pix, y_pix, x_pix + pixel_len[0], y_pix + pixel_len[1],
                                outline=outline, fill=color, width=outline_width)

    # création du Black & White
    canvas.delete('all')
    for tile in laby.tiles:
        if tile.path is not None:
            make_pix(tile, 'white')
        elif len(tile.voisins) in [2, 3]:
            make_pix(tile, '#8F000C')

    grad = int_to_grad_hexa(len(laby.lists.distances))

    if mode == 'B&W':
        pass

    elif mode == 'deadlocks':
        print(len(laby.lists.deadlocks))
        for tile in laby.lists.deadlocks:
            make_pix(tile, 'grey')

    elif mode == 'distance':

        for distance, tile_list in laby.lists.distances.items():
            for tile in tile_list:
                canvas.itemconfig(tile.print_rectangle, fill=grad[distance - 1])
            canvas.update()
            # sleep(0.01)

    elif mode == 'solution':
        for tile in laby.lists.solutions:
            make_pix(tile, grad[tile.distance - 1])

    else:
        raise Exception(f"mode {mode} for screen() not reconize.")

    make_pix(laby.tile_start, '', grad[-1])
    make_pix(laby.tile_arrival, '', grad[0])
