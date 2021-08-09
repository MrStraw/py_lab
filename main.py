import sys

from models.labyrinth import Labyrinth

a = 10
tup = (int(1920 / a), int(1080 / a))
sys.setrecursionlimit(3000)
# TODO .export, grad couleur vert a rouge (adapatable), bug set_X_tile trop grand (meme apres verif), square
laby = Labyrinth(shape=tup,
                 # seed='?lNe#Hh#i69_Y17QzT_o',
                 methode='hole',
                 complexity=0.1,
                 stop_to_step='deadlock',
                 set_start_tile=(55, 5),
                 set_arrival_tile=(200, 100)
                 )
print(laby.seed)

laby.screen(mode='distance',
            fullscreen=True,
            # display='square'
            )
