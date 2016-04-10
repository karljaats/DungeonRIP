from character import Character
from pathfinder import find_path


class Monster(Character):
    def __init__(self, x, y, images):
        super().__init__(x, y, images, "monster")

        self.alert_range = 10

    def update(self, map, player):
        if player.x in [self.x-1, self.x, self.x+1] and player.y in [self.y-1, self.y, self.y+1]:
            player.take_damage(self.attack)
        elif self.x - self.alert_range < player.x < self.x + self.alert_range and self.y - self.alert_range < player.y < self.y + self.alert_range:
            # find_path([self.x, self.y], [player.x, player.y], map)
            pass
