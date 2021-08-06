from models.labyrinth import Labyrinth
from utils.print_t import print_t

laby = Labyrinth(shape=(120, 50),
                 methode='full')

# print_t(laby.table, 'distance')

laby.screen('impasses')


# TODO seed, % de fusion, arrive et depart, thread screen()