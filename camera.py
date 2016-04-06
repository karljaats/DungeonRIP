class Camera:
    def __init__(self, screen_w, screen_h, tile_size, x=0, y=0):
        self.x = x
        self.y = y
        self.overlay_bottom_h = 0
        self.overlay_side_w = 0
        self.width = screen_w - self.overlay_side_w
        self.height = screen_h - self.overlay_bottom_h
        self.tile_size = tile_size

    def draw(self, screen, map, monsters, player):
        """
        joonistab kõik ekraanile
        :param screen: aken
        :param map: kaart, listina
        :param characters: dictionary elusolenditest, praegu ainult mängija
        :return: aken
        """
        # joonista kaart
        for x in range(0, self.width):
            for y in range(0, self.height):
                tile_type = map.map[self.x + x][self.y + y]
                destination = (x*self.tile_size, y*self.tile_size)
                screen.blit(map.objects[tile_type]["image"], destination)

        # joonista mängija
        screen.blit(player.image, ((player.x-self.x)*self.tile_size, (player.y-self.y)*self.tile_size))
        health_amount = player.current_health / player.max_health
        screen.fill((255, 0, 0), ((player.x-self.x)*self.tile_size, (player.y-self.y)*self.tile_size+18, 20, 2))
        screen.fill((0, 255, 0), ((player.x-self.x)*self.tile_size, (player.y-self.y)*self.tile_size+18, 20*health_amount, 2))

        # joonista vaenlased
        for monster in monsters:
            # On see ekraanil
            if self.x + self.width > monster.x >= self.x and self.y + self.height > monster.y >= self.y:
                screen.blit(monster.image, ((monster.x-self.x)*self.tile_size, (monster.y-self.y)*self.tile_size))
                health_amount = monster.current_health / monster.max_health
                screen.fill((255, 0, 0), ((monster.x-self.x)*self.tile_size, (monster.y-self.y)*self.tile_size+18, 20, 2))
                screen.fill((0, 255, 0), ((monster.x-self.x)*self.tile_size, (monster.y-self.y)*self.tile_size+18, 20*health_amount, 2))

    def center(self, map_width, map_height, player_x, player_y):
        """
        Muuda kaamera asukohta nii, et mängija on pildi keskel
        :param map_width: kaardi laius, tile'ides
        :param map_height: kaardi kõrgus, tile'ides
        :param player_x: mängija x koordinaat, kaardi koordinaatides
        :param player_y: mängija y koordinaat, kaardi koordinaatides
        """
        x = player_x - self.width//2
        y = player_y - self.height//2

        if map_width - self.width >= x:
            if x >= 0:
                self.x = x
            else:
                self.x = 0
        else:
            self.x = map_width - self.width

        if map_height - self.height >= y:
            if y >= 0:
                self.y = y
            else:
                self.y = 0
        else:
            self.y = map_height - self.height
