import tkinter as tk

from models import _Tile

from models.labyrinth.simplify import *
from utils import int_to_grad_hexa


def print_mode(laby: 'Labyrinth', canvas: tk.Canvas, pixel_len: int, mode: str = 'B&W'):
    if mode not in ['B&W', 'distance', 'solution', 'impasses']:
        raise Exception(f"mode {mode} for screen() not reconize.")

    # création du Black & White
    canvas.delete('all')
    for tile in laby.tiles:
        x_pix = tile.x * pixel_len
        y_pix = tile.y * pixel_len
        if tile.path:
            canvas.create_rectangle(x_pix, y_pix, x_pix + pixel_len, y_pix + pixel_len,
                                    outline='', fill='white')

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
                color = grad[tile.distance - 1]

        elif mode == 'impasses':
            if tile.deadlock:
                color = 'grey'

        canvas.create_rectangle(x_pix, y_pix, x_pix + pixel_len, y_pix + pixel_len,
                                outline='', fill=color)
