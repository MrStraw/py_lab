from models.labyrinth import Labyrinth

a = 10
tup = (int(1920/a), int(1080/a))

laby = Labyrinth(shape=tup,
                 methode='hole',
                 break_proba=0.4)

laby.screen('distance')

# TODO seed, arrive et depart, thread screen()
