import random

"""

VANA VERSIOON,
ei sobi uue struktuuriga,
uus versioon on map2.py-s.

"""
class Map:
    def __init__(self, images):
        self.map = None
        self.images = images
        self.width = 0
        self.height = 0

    # based on http://www.roguebasin.com/index.php?title=Dungeon-Building_Algorithm
    # randomly picks tiles until it finds a wall of a room
    # and puts a random "feature" there if there's room for it
    def generate_map(self, size_x=100, size_y=100):
        self.width = size_x
        self.height = size_y

        # how many tries should be made
        tries = 100

        self.map = {}

        # for probabilities
        feature_list = self.create_feature_list()

        # fill everything with wall
        for x in range(0, size_x):
            for y in range(0, size_y):
                if x == 0 or x == size_x-1 or y == 0 or y == size_y-1:
                    self.map[(x, y)] = "outer_wall"
                else:
                    self.map[(x, y)] = "wall"

        # create center room
        width = random.randint(4, 10)
        height = random.randint(4, 10)
        for x in range(0, width):
            for y in range(0, height):
                self.map[(self.width//2 - width//2 + x, self.height//2 - height//2 + y)] = "floor"

        # create the map
        for i in range(tries):
            found_suitable_wall = False
            # find a suitable wall
            while not found_suitable_wall:
                x = random.randint(0, self.width-1)
                y = random.randint(0, self.height-1)
                # suitable if it is a wall and at least one adjacent tile is not a wall
                if self.map[(x, y)] == "wall":
                    if self.map[(x+1, y)] == "floor" or self.map[(x-1, y)] == "floor" or self.map[(x, y+1)] == "floor"\
                            or self.map[(x, y-1)] == "floor":
                        found_suitable_wall = True

            # pick a feature
            feature = feature_list[random.randint(0, len(feature_list)-1)]

            # pick a direction
            if self.map[(x+1, y)] == "floor":
                direction = "W"
            elif self.map[(x-1, y)] == "floor":
                direction = "E"
            elif self.map[(x, y+1)] == "floor":
                direction = "N"
            elif self.map[(x, y-1)] == "floor":
                direction = "S"

            # get feature dimensions
            # feature_width and height count walls too
            if feature == "room":
                feature_width = random.randint(6, 12)
                feature_height = random.randint(6, 12)
            elif feature == "corridor":
                if direction == "N" or direction == "S":
                    feature_width = 3
                    feature_height = random.randint(7, 17)
                if direction == "E" or direction == "W":
                    feature_width = random.randint(7, 17)
                    feature_height = 3

            if feature != "corridor":
                # get the coordinates that it takes over
                if direction == "N":
                    top_left = (x-feature_width//2, y-(feature_height-1))
                    if feature_width % 2 == 0:
                        bottom_right = (x+feature_width//2-1, y)
                    else:
                        bottom_right = (x+feature_width//2, y)

                elif direction == "E":
                    top_left = (x, y-feature_height//2)
                    if feature_height % 2 == 0:
                        bottom_right = (x+(feature_width-1), y+feature_height//2-1)
                    else:
                        bottom_right = (x+(feature_width-1), y+feature_height//2)
                elif direction == "S":
                    top_left = (x-feature_width//2, y)
                    if feature_width % 2 == 0:
                        bottom_right = (x+feature_width//2-1, y+(feature_height-1))
                    else:
                        bottom_right = (x+feature_width//2, y+(feature_height-1))
                elif direction == "W":
                    top_left = (x-(feature_width-1), y-feature_height//2)
                    if feature_height % 2 == 0:
                        bottom_right = (x, y+feature_height//2-1)
                    else:
                        bottom_right = (x, y+feature_height//2)

                # check if there is enough room to put the feature
                if not 0 < top_left[0] < self.width or not 0 < top_left[1] < self.height or not 0 < bottom_right[0]\
                        < self.width or not 0 < bottom_right[1] < self.height:
                    continue
                enough_room = True
                for k in range(bottom_right[0] - top_left[0] + 1):  # +1s are because of coordinate subtraction...
                    for j in range(bottom_right[1] - top_left[1] + 1):  # ...weirdness
                        if self.map[(top_left[0]+k, top_left[1]+j)] != "wall":
                            enough_room = False
                            break
                    if not enough_room:
                        break

                # if no room start again
                if not enough_room:
                    continue

                # write the changes to the map
                self.map[(x, y)] = "floor"  # the door tile
                for k in range(bottom_right[0] - top_left[0] - 1):  # -1s are to take out the walls of the feature
                    for j in range(bottom_right[1] - top_left[1] - 1):  # and coordinate subtraction works weirdly
                        self.map[(top_left[0]+1+k, top_left[1]+1+j)] = "floor"

            # if it is a corridor we want
            # corridor is different because if it intercepts other stuff we want to still make it, but only to
            # the point where it met the other thing
            else:
                if direction == "N":
                    for k in range(feature_height):
                        if self.map[(x-1, y - k)] != "wall" or self.map[(x, y - k)] != "wall" \
                                        or self.map[(x+1, y - k)] != "wall":
                            if self.map[(x-1, y - k)] == "outer_wall" or self.map[(x, y - k)] == "outer_wall" \
                                        or self.map[(x+1, y - k)] == "outer_wall":
                                break
                            else:
                                self.map[(x, y - k)] = "floor"
                                break
                        else:
                            self.map[(x, y - k)] = "floor"
                if direction == "E":
                    for k in range(feature_width):
                        if self.map[(x + k, y-1)] != "wall" or self.map[(x + k, y)] != "wall" \
                                        or self.map[(x + k, y+1)] != "wall":
                            if self.map[(x + k, y-1)] == "outer_wall" or self.map[(x + k, y)] == "outer_wall" \
                                        or self.map[(x + k, y+1)] == "outer_wall":
                                break
                            else:
                                self.map[(x + k, y)] = "floor"
                                break
                        else:
                            self.map[(x + k, y)] = "floor"
                if direction == "S":
                    for k in range(feature_height):
                        if self.map[(x-1, y + k)] != "wall" or self.map[(x, y + k)] != "wall" \
                                        or self.map[(x+1, y + k)] != "wall":
                            if self.map[(x-1, y + k)] == "outer_wall" or self.map[(x, y + k)] == "outer_wall" \
                                        or self.map[(x+1, y + k)] == "outer_wall":
                                break
                            else:
                                self.map[(x, y + k)] = "floor"
                                break
                        else:
                            self.map[(x, y + k)] = "floor"
                if direction == "W":
                    for k in range(feature_width):
                        if self.map[(x - k, y-1)] != "wall" or self.map[(x - k, y)] != "wall" \
                                        or self.map[(x - k, y+1)] != "wall":
                            if self.map[(x - k, y-1)] == "outer_wall" or self.map[(x - k, y)] == "outer_wall" \
                                        or self.map[(x - k, y+1)] == "outer_wall":
                                break
                            else:
                                self.map[(x - k, y)] = "floor"
                                break
                        else:
                            self.map[(x - k, y)] = "floor"

        # change names for objects
        for i in self.map:
            name = self.map[i]
            if name == "wall":
                self.map[i] = Wall(i[0], i[1], self.images["wall"])
            elif name == "outer_wall":
                self.map[i] = OuterWall(i[0], i[1], self.images["wall"])
            elif name == "floor":
                self.map[i] = Floor(i[0], i[1], self.images["floor"])

    def create_feature_list(self):
        # creates a list of "features" for the map to be used with the random number generator
        # the list has the members multiple times in conjunction with their probabilities
        list = []

        # does not have to add up to 100, can be anything
        probabilities = {
                    "room": 70,
                    "corridor": 30
                }

        for feature in probabilities:
            for i in range(probabilities[feature]):
                list.append(feature)

        return list
