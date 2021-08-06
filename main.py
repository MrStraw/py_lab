import sys

from models.labyrinth import Labyrinth

a = 9
tup = (int(1920 / a), int(1080 / a))
sys.setrecursionlimit(3000)

# TODO arrive et depart, thread screen(), affichage seed, .export

laby = Labyrinth(shape=tup,
                 seed=None,
                 methode='hole',
                 complexity=0.07,
                 stop_to_step='deadlock'
                 )
print(laby.seed)
laby.screen(mode='B&W',
            fullscreen=False,
            display='square')
