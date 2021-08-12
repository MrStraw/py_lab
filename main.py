import sys

from models.labyrinth import Labyrinth

a = 5
tup = (int(1920 / a), int(1080 / a))
sys.setrecursionlimit(3000)
# TODO .export, grad couleur vert a rouge (adapatable), bug set_X_tile trop grand (meme apres verif), square ,
laby = Labyrinth(shape=(320, 180),
                 # seed='zRyb5Y}w5Gn*n+NoQdY:',   # seed de fdp: hILfu*dYZ]N0+EK1o6`M
                 methode='hole',
                 complexity=0.1,
                 stop_to_step='deadlock',
                 set_start_tile=(60, 90),
                 set_arrival_tile=(260, 90)
                 )
print(laby.seed)

laby.screen(mode='distance',
            fullscreen=True,
            # display='square'
            )
