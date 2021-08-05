import tkinter as tk

from models import _Tile

from models.labyrinth.simplify import *


def print_mode(laby: 'Labyrinth', canvas: tk.Canvas, pixel_len: int, mode: str = 'B&W'):

    for t in laby.tiles:
        tile: _Tile = t
        x_pix = tile.x * pixel_len
        y_pix = tile.y * pixel_len
        color = 'white' if tile.path else 'black'
        canvas.create_rectangle(x_pix, y_pix, x_pix + pixel_len, y_pix + pixel_len,
                                outline='red', fill=color)

