from models.labyrinth.generate_steps.init_table import init_table
from models.labyrinth.generate_steps.make_path import one_shot_the_path
from models.labyrinth.simplify import *


def all_step(laby: 'Labyrinth'):
    init_table(laby)
    one_shot_the_path(laby)
