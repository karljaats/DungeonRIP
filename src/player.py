from character import Character


class Player(Character):
    def __init__(self, x, y, images):
        super().__init__(x, y, images, "player")

        self.max_health = 20
        self.current_health = self.max_health

    def move(self, dif_x, dif_y, map):
        """
        Liigu antud suunas
        :param dif_x: muutus x suunas
        :param dif_y: muutus y suunas
        :param map: kaart
        :return: None
        """
        if map.objects[map.map[self.x + dif_x][self.y + dif_y]]["passable"]:
            self.x += dif_x
            self.y += dif_y
