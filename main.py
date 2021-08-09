import sys

from models.labyrinth import Labyrinth

a = 5
tup = (int(1920 / a), int(1080 / a))
sys.setrecursionlimit(3000)
# TODO .export, solution bug, grad couleur vert a rouge (adapatable), bug set_X_tile trop grand (meme apres verif)
laby = Labyrinth(shape=tup,
                 # seed='?lNe#Hh#i69_Y17QzT_o',
                 methode='hole',
                 complexity=0.1,
                 stop_to_step='deadlock',
                 set_start_tile=(20, 12),
                 set_arrival_tile=(300, 200)
                 )
print(laby.seed)

laby.screen(mode='distance',
            fullscreen=True,
            # display='square'
            )
