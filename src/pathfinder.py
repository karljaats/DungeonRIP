def find_path(start, end, map):
    nodes = []
    for x in map.width:
        for y in map.height:
            if map.objects[map.map[x][y]]["passable"]:
                reachable = True
            else:
                reachable = False
            nodes.append(Node(x, y, reachable))

    open_list = []
    closed_list = set()
    open_list.append((start[0], start[1]))

    while True:
        min_f = 9999
        min_pos = [0, 0]
        for pos in open_list:
            node = nodes[pos[0]][pos[1]]
            if node.f < min_f:
                min_f = node.f
                min_pos = (node.x, node.y)

        current = nodes[pos[0]][pos[1]]





class Node:
    def __init__(self, x, y, reachable):
        self.x = x
        self.y = y
        self.reachable = reachable
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
