class Camera:
    def __init__(self, screen_w, screen_h, tile_size, font, x=0, y=0):
        self.x = x
        self.y = y
        self.width = screen_w
        self.height = screen_h
        self.tile_size = tile_size
        self.font = font

    def draw(self, screen, map, monsters, player):
        """
        joonistab kõik ekraanile
        :param screen: aken
        :param map: kaart, listina
        :param monsters: dictionary vaenlastest
        :param player: mängija objekt
        :return: aken
        """
        # joonista kaart
        for x in range(0, self.width):
            for y in range(0, self.height-2):
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

        # joonista riba info jaoks
        screen.fill((0, 0, 0), (0, (self.height-2)*self.tile_size, self.width*self.tile_size, 40))
        screen.fill((127, 127, 127), (0, (self.height-2)*self.tile_size, self.width*self.tile_size, 2))
        screen.blit(self.font.render("Health: " + str(player.current_health) + "/" + str(player.max_health), True, (255, 255, 255)), (10, (self.height-2)*self.tile_size+10))
        screen.blit(self.font.render("L" + str(map.level), True, (255, 255, 255)), (self.width*self.tile_size-60, (self.height-2)*self.tile_size+10))

    def center(self, map_width, map_height, player_x, player_y):
        """
        Muuda kaamera asukohta nii, et mängija on pildi keskel
        :param map_width: kaardi laius, tile'ides
        :param map_height: kaardi kõrgus, tile'ides
        :param player_x: mängija x koordinaat, kaardi koordinaatides
        :param player_y: mängija y koordinaat, kaardi koordinaatides
        :return: None
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
