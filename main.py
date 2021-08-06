from models.labyrinth import Labyrinth

a = 40
tup = (int(1920 / a), int(1080 / a))

laby = Labyrinth(shape=tup,
                 seed='test',
                 methode='hole',
                 complexity=0.4,
                 )

laby.screen('distance')

# TODO seed, arrive et depart, thread screen()
