class Character:
    def __init__(self, x, y, images, name):
        self.image = images[name]
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.x = x  # tiledes, mitte pixlites
        self.y = y

        self.max_health = 5
        self.current_health = self.max_health
        self.attack = 1

    def take_damage(self, damage):
        """
        Kui tegelane saab haiget
        :param damage: damage hulk
        :return: None
        """
        self.current_health -= damage
