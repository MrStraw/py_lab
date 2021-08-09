import tkinter as tk
from screeninfo import get_monitors
import pyperclip

from .print_mode import print_mode

from models.labyrinth.simplify import *


def screen_lab(laby: 'Labyrinth', mode: str, fullscreen: bool, display: str):

    window = tk.Tk()
    window.title("Auto labyrinth")
    window.configure(background='black')
    window.attributes('-fullscreen', fullscreen)

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
    s_height -= 30
    window.geometry(f"{s_width}x{s_height}")
    if not fullscreen:
        s_width -= 70
        s_height -= 40

    # taille des pixels
    pixel_len_width = s_width / laby.width
    pixel_len_height = s_height / laby.height
    if min(pixel_len_height, pixel_len_width) < 1:
        raise Exception("Labyrinth to big for the screen")  # TODO afficher la taille min
    if display == 'spread out':
        pixel_len = (pixel_len_width, pixel_len_height)
    elif display == 'square':
        pixel_len = min(pixel_len_height, pixel_len_width)
        pixel_len = (pixel_len, pixel_len)
    else:
        raise Exception("Bad option for 'display'.")

    window.minsize(round(pixel_len[0] * laby.width), round(pixel_len[1] * laby.height))

    # Création du canva
    canvas = tk.Canvas(window, width=s_width, height=s_height, bg='black')
    canvas.pack()

    def simple_sprint(modee=mode):
        print_mode(laby, canvas, pixel_len, modee)

    # affichage du lab en noir et blanc
    simple_sprint()

    # Menu print
    menu = tk.Menu(window)
    menu_print = tk.Menu(menu, tearoff=0)
    # menu_print.add_command(label="Créer un nouveau labyrinthe", command=lambda: generate(laby, canvas))
    # menu_print.add_separator()
    menu_print.add_command(label="Classique", command=lambda: simple_sprint('B&W'))
    menu_print.add_command(label="Solution", command=lambda: simple_sprint('solution'))
    menu_print.add_command(label="Voir les impasses", command=lambda: simple_sprint('deadlocks'))
    # menu_print.add_command(label="Tous les chemins", command=lambda: simple_sprint('tout chemins'))
    menu_print.add_command(label="Gradiant des distances", command=lambda: simple_sprint('distance'))
    # menu_print.add_command(label="Tout les chemins en gradiant", command=lambda: simple_sprint('grad sans impasse'))
    menu.add_cascade(label="Print mode", menu=menu_print)
    # Menu seed
    menu_seed = tk.Menu(menu, tearoff=0)
    menu_seed.add_command(label=f"Copy the seed : '{laby.seed}'", command=lambda: pyperclip.copy(laby.seed))
    menu.add_cascade(label="Seed", menu=menu_seed)

    window.config(menu=menu)
    window.mainloop()
