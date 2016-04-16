from character import Character
from pathfinder import find_path


class Monster(Character):
    def __init__(self, x, y, images):
        super().__init__(x, y, images, "monster")

        self.alert_range = 10

    def update(self, map, player, monsters):
        """
        vaenlase käik
        :param map: kaart
        :param player: mängija
        :param monsters: list kõigist vaenlastest
        :return: None
        """
        if player.x in [self.x-1, self.x, self.x+1] and player.y in [self.y-1, self.y, self.y+1]:
            player.take_damage(self.attack)
        elif self.x - self.alert_range < player.x < self.x + self.alert_range and self.y - self.alert_range < player.y < self.y + self.alert_range:
            new_pos = find_path([self.x, self.y], [player.x, player.y], map)
            for monster in monsters:
                if (monster.x, monster.y) == new_pos:
                    return
            self.x = new_pos[0]
            self.y = new_pos[1]
