from .init_table import init_table
from .make_path import make_path

from models.labyrinth.simplify import *


def all_step(laby: 'Labyrinth'):
    init_table(laby)
    make_path(laby)
