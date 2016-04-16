def find_path(start, end, map):
    """
    Leia kõige otsem tee, kasutab A* algoritmi
    :param start: algus punkti koordinaadid
    :param end: lõpp punkti koordinaadid
    :param map: kaart
    :return: Tee kõige esimese sammu koordinaadid
    """
    start = (start[0], start[1])
    end = (end[0], end[1])

    # läbi vaadatud node'd
    closed = set()
    # veel läbi vaatamata node'd
    opened = [start]
    # iga node kõige efektiivsem koht kust sinna saab
    came_from = {}
    # iga node jaoks hind algusest selleni liikumiseks
    g_score = {}
    g_score.setdefault(float("inf"))
    g_score[start] = 0
    # iga node hinnatav hind lõppu jõudmiseks
    f_score = {}
    f_score.setdefault(float("inf"))
    f_score[start] = heuristic_cost(start, end)

    while len(opened) != 0:
        current = opened[0]
        for node in opened:
            if f_score[current] > f_score[node]:
                current = node

        if current == end:
            return reconstruct_path(came_from, current)

        opened.remove(current)
        closed.add(current)

        x = current[0]
        y = current[1]

        neighbours = []
        if x > 0:
            neighbours.append([x-1, y])
        if x < map.width-1:
            neighbours.append([x+1, y])
        if y > 0:
            neighbours.append([x, y-1])
        if y < map.height-1:
            neighbours.append([x, y+1])
        if x > 0 and y > 0:
            neighbours.append([x-1, y-1])
        if x < map.width-1 and y < map.height-1:
            neighbours.append([x+1, y+1])
        if x < map.width-1 and y > 0:
            neighbours.append([x+1, y-1])
        if x > 0 and y < map.height-1:
            neighbours.append([x-1, y+1])

        g = g_score[current] + 1
        for neighbour in neighbours:
            neighbour = (neighbour[0], neighbour[1])
            if not map.objects[map.map[neighbour[0]][neighbour[1]]]["passable"]:
                continue
            if neighbour in closed:
                continue

            if neighbour not in opened:
                opened.append(neighbour)
            elif g >= g_score[neighbour]:
                continue

            came_from[neighbour] = current
            g_score[neighbour] = g
            f_score[neighbour] = g + heuristic_cost(neighbour, end)


def heuristic_cost(start, goal):
    """
    pakutav tee pikkus lõpp punkti
    :param start: alguspunkt
    :param goal: lõpppunkt
    :return: tee pikkus ehk hind
    """
    vector = [abs(start[0]-goal[0]), abs(start[1] - goal[1])]
    diagonal_movement = min(vector)
    other_movement = abs(vector[0]-vector[1])
    return diagonal_movement + other_movement


def reconstruct_path(came_from, current):
    """
    Lõpppunktist tagsi kõige efektiivsema tee konstrueerimine
    :param came_from: dictionary kõigist tiledest ja kuidas nendele kõige efektiivsemalt saab
    :param current: lõpppunkt
    :return: Kõige esimese sammu koordinaadid
    """
    total_path = []
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    total_path.pop()
    return total_path.pop()
