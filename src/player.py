from src.character import Character


class Player(Character):
    def __init__(self, x, y, images):
        super().__init__(x, y, images, "player")

        self.max_health = 20
        self.current_health = self.max_health
        self.attack = 2

        self.regen_time = 5
        self.regen_timer = self.regen_time

    def move(self, dif_x, dif_y, map, monsters):
        """
        Liigu antud suunas
        :param dif_x: muutus x suunas
        :param dif_y: muutus y suunas
        :param map: kaart
        :return: None
        """
        is_monster = False
        for monster in monsters:
            if self.x + dif_x == monster.x and self.y + dif_y == monster.y:
                monster.take_damage(self.attack)
                is_monster = True
        if not is_monster and map.objects[map.map[self.x + dif_x][self.y + dif_y]]["passable"]:
            self.x += dif_x
            self.y += dif_y

    def update(self):
        """
        elu regenereerimine
        :return: None
        """
        if self.current_health < self.max_health:
            self.regen_timer -= 1
            if self.regen_timer == 0:
                self.current_health += 1
                self.regen_timer = self.regen_time
