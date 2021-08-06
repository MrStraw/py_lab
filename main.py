import sys

from models.labyrinth import Labyrinth

a = 20
tup = (int(1920 / a), int(1080 / a))
sys.setrecursionlimit(3000)

# TODO arrive et depart, thread screen()

laby = Labyrinth(shape=tup,
                 seed=None,
                 methode='hole',
                 complexity=0.10,
                 )
laby.screen()

