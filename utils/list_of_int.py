import random


def list_of_int(number: int):
    pile = []
    for i in range(1, number + 1):
        pile.append(i)
    random.shuffle(pile)
    return pile
