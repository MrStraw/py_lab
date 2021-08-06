from models import Tile


def print_t(table, mode: str = 'couleur'):
    l_ligne = table.shape[0]
    l_colone = table.shape[1]

    if mode == 'couleur':
        print(table)

    elif mode == 'distance':
        arrive: Tile = table[l_ligne - 2, l_colone - 1]
        t = len(str(arrive.distance))
        s = ''
        for lignes in table:
            s += '\n'
            for case in lignes:
                s2 = ''
                if case.is_arrival:
                    s2 += "A"
                elif case.is_start:
                    s2 += "D"
                elif case.path:
                    if case.distance == 0:
                        s2 += '*'
                    else:
                        s2 += str(case.distance)
                else:
                    s2 += ' '

                while len(s2) < t:
                    if case.is_start:
                        s2 += "A"
                    elif case.is_start:
                        s2 += "D"
                    elif case.path:
                        if case.distance == 0:
                            s2 += '*'
                        else:
                            s2 = '0' + s2
                    else:
                        s2 += ' '
                s += s2 + ' '
        print(s)

    else:
        s = ''
        for ligne in table:
            s += '\n'
            for case in ligne:
                if not case.path:
                    wall_neig = search_wall_around(case)
                    if wall_neig == [1, 0, 1, 0]:
                        s += '═══'
                    elif wall_neig == [1, 0, 0, 0]:
                        s += ' ══'
                    elif wall_neig == [0, 0, 1, 0]:
                        s += '══ '
                    elif wall_neig == [0, 1, 0, 0] or wall_neig == [0, 0, 0, 1] or wall_neig == [0, 1, 0, 1]:
                        s += ' ║ '
                    elif wall_neig == [1, 0, 0, 1]:
                        s += ' ╚═'
                    elif wall_neig == [0, 0, 1, 1]:
                        s += '═╝ '
                    elif wall_neig == [0, 1, 1, 0]:
                        s += '═╗ '
                    elif wall_neig == [1, 1, 0, 0]:
                        s += ' ╔═'
                    elif wall_neig == [1, 0, 1, 1]:
                        s += '═╩═'
                    elif wall_neig == [1, 1, 1, 0]:
                        s += '═╦═'
                    elif wall_neig == [1, 1, 0, 1]:
                        s += ' ╠═'
                    elif wall_neig == [1, 1, 1, 1]:
                        s += '═╬═'
                    elif wall_neig == [0, 1, 1, 1]:
                        s += '═╣ '
                    elif wall_neig == [0, 0, 0, 0]:
                        s += ' ■ '
                else:
                    if mode == 'lab':
                        s += '   '
                    elif mode == 'solution':
                        if case.solution == 1:
                            s += ' · '
                        else:
                            s += '   '
                    elif mode == 'full_path':
                        if case.solution == 1:
                            s += ' · '
                        elif case.full_path:
                            s += '   '
                        else:
                            s += ' x '
        print(s)


def search_wall_around(tile: Tile):
    table = tile.table
    l_ligne = table.shape[0]
    l_colone = table.shape[1]
    tableau = tile.table
    if tile.location == (0, 0):
        return [1, 0, 1, 0]
    if tile.location == (2, 0):
        return [0, 1, 1, 0]
    if tile.location == (l_ligne - 3, l_colone - 1):
        return [1, 0, 0, 1]
    if tile.location == (l_ligne - 1, l_colone - 1):
        return [1, 0, 1, 0]

    tuples = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    liste_voisin = [0, 0, 0, 0]
    for i, t in enumerate(tuples):
        ligne_v = t[0] + tile.x
        colone_v = t[1] + tile.y
        try:
            case_voisine: Tile = tableau[ligne_v, colone_v]
        except IndexError:
            continue
        if 0 > ligne_v > l_ligne - 1 or 0 > colone_v > l_colone - 1:
            continue
        if not case_voisine.path:
            liste_voisin[i] = 1
        if tile.x == 0:
            liste_voisin[3] = 0
        if tile.y == 0:
            liste_voisin[2] = 0
    return liste_voisin
