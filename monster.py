from character import Character


class Monster(Character):
    def __init__(self, x, y, images):
        super().__init__(x, y, images, "monster")
