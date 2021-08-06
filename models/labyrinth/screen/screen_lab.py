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

    def simple_sprint(modee=mode):
        print_mode(laby, canvas, pixel_len, modee)

    # affichage du lab en noir et blanc
    simple_sprint()

    # Menu
    menu = tk.Menu(window)
    menu_print = tk.Menu(menu, tearoff=0)
    # menu_print.add_command(label="Créer un nouveau labyrinthe", command=lambda: generate(laby, canvas))
    menu_print.add_separator()
    menu_print.add_command(label="Classique", command=lambda: simple_sprint('B&W'))
    menu_print.add_command(label="Solution", command=lambda: simple_sprint('solution'))
    menu_print.add_command(label="Voir les impasses", command=lambda: simple_sprint('impasses'))
    # menu_print.add_command(label="Tous les chemins", command=lambda: simple_sprint('tout chemins'))
    menu_print.add_command(label="Gradiant des distances", command=lambda: simple_sprint('distance'))
    # menu_print.add_command(label="Tout les chemins en gradiant", command=lambda: simple_sprint('grad sans impasse'))
    menu.add_cascade(label="Print mode", menu=menu_print)

    window.config(menu=menu)
    window.mainloop()
