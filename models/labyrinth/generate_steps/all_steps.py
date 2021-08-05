from models.labyrinth.generate_steps.init_table import init_table
from models.labyrinth.generate_steps.make_path import one_shot_the_path
from models.labyrinth.generate_steps.mesure_distance import mesure_distance
from models.labyrinth.generate_steps.resoudre_lab import resoudre_lab
from models.labyrinth.simplify import *


def all_step(laby: 'Labyrinth'):

    print('Initialization du tableau')
    init_table(laby)

    print("Création du chemin")
    one_shot_the_path(laby)

    print("Mesure des distances")
    mesure_distance(laby)

    print("Résolution du labyrinthe")
    resoudre_lab(laby)

    print("Done")
