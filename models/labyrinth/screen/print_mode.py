import tkinter as tk

from models import _Tile

from models.labyrinth.simplify import *
from utils import int_to_grad_hexa


def print_mode(laby: 'Labyrinth', canvas: tk.Canvas, pixel_len: int, mode: str = 'B&W'):
    if mode not in ['B&W', 'distance', 'solution']:
        raise Exception(f"mode {mode} for screen() not reconize.")

    for t in laby.tiles:
        tile: _Tile = t
        x_pix = tile.x * pixel_len
        y_pix = tile.y * pixel_len
        color = 'white' if tile.path else 'black'
        canvas.create_rectangle(x_pix, y_pix, x_pix + pixel_len, y_pix + pixel_len,
                                outline='', fill=color)

    if mode == 'B&W':
        return

    grad = int_to_grad_hexa(laby.tile_arrival.distance)
    for tile in laby.path.tiles:
        color = 'white'
        x_pix = tile.x * pixel_len
        y_pix = tile.y * pixel_len

        if mode == 'distance':
            if tile.distance:
                color = grad[tile.distance - 1]

        elif mode == 'solution':
            if tile.is_solution:
                color = 'red'
                # color = grad[tile.distance - 1]

        canvas.create_rectangle(x_pix, y_pix, x_pix + pixel_len, y_pix + pixel_len,
                                outline='', fill=color)
