from models.labyrinth.generate_steps.impasses import impasses
from models.labyrinth.generate_steps.init_table import init_table
from models.labyrinth.generate_steps.make_path import one_shot_the_path
from models.labyrinth.generate_steps.mesure_distance import mesure_distance
from models.labyrinth.generate_steps.resoudre_lab import resoudre_lab
from models.labyrinth.generate_steps.set_start_and_arrival import set_start_and_arrival
from models.labyrinth.simplify import *


def all_step(laby: 'Labyrinth'):
    if laby._stop_to_step not in ['distance', 'solution', 'deadlock', 'all']:
        raise Exception('Option stop_to_step not reconize')

    print('Initialization du tableau')
    init_table(laby)
    set_start_and_arrival(laby)
    one_shot_the_path(laby)

    if laby._stop_to_step == 'distance':
        print("Done")
        return
    print("Mesure des distances")
    mesure_distance(laby)

    if laby._stop_to_step == 'solution':
        pass
    else:
        print("Résolution du labyrinthe")
        resoudre_lab(laby)

    if laby._stop_to_step == 'deadlock':
        pass
    else:
        print("Calcul des impasses")
        impasses(laby)

    print("Done")
