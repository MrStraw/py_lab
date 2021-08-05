import tkinter as tk
from screeninfo import get_monitors

from .print_mode import print_mode

from models.labyrinth.simplify import *


def screen_lab(laby: 'Labyrinth', mode: str):

    window = tk.Tk()
    window.title("Auto labyrinth")
    window.configure(background='black')
    # window.attributes('-fullscreen', True)

    # Recherche du plus grand écran
    length = 0
    s_height = 0
    s_width = 0
    for m in get_monitors():
        m_length = m.height * m.width
        if m_length > length:
            length = m_length
            s_width = m.width
            s_height = m.height
    window.geometry(f"{s_width}x{s_height}")
    s_height -= 60
    s_width -= 60
    window.minsize(s_width, s_height)

    # taille des pixels
    pixel_len_width = int(s_width / laby.width)
    pixel_len_height = int(s_height / laby.height)
    pixel_len: int = min(pixel_len_height, pixel_len_width)
    if pixel_len < 2:
        raise Exception("Labyrinth to big for the screen")  # TODO afficher la taille min

    # Création du canva
    canvas = tk.Canvas(window, width=s_width, height=s_height, bg='black')
    canvas.pack()

    def simple_sprint():
        print_mode(laby, canvas, pixel_len, mode)

    # affichage du lab en noir et blanc
    simple_sprint()

    window.mainloop()
