from models.labyrinth.generate_steps.init_table import init_table
from models.labyrinth.generate_steps.make_path import one_shot_the_path
from models.labyrinth.generate_steps.mesure_distance import mesure_distance
from models.labyrinth.simplify import *


def all_step(laby: 'Labyrinth'):
    init_table(laby)
    one_shot_the_path(laby)
    mesure_distance(laby)

