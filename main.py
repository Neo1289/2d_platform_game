###LIBRARIES
from libraries_and_settings import (pygame,
                                    sys)
###CONFIGURATIONS
from libraries_and_settings import (display_surface, maps)

###SPRITES
from player import Player
from camera import allSpritesOffset

pygame.init()

class Game:
    def __init__(self):

        self.running = True
        self.display_surface = display_surface
        self.clock = pygame.time.Clock()

        self.maps = maps
        self.current_map = None
        self.current_area = "world"

        self.collision_sprites = pygame.sprite.Group()
        self.all_sprites = allSpritesOffset

        self.player = None

    def mapping(self):

        for name, map in self.maps.items():
            if name == self.current_area:
                self.current_map = map

        ###ground
        for x, y, image in self.current_map.get_layer_by_name('ground').tiles():
            print(x,y,image)
        ###objects
        for obj in self.current_map.get_layer_by_name('objects'):
            print(obj.name)

        ###player
        for obj in self.current_map.get_layer_by_name('areas'):
            if obj.name == 'player_spawn':
                if self.player is None:
                    self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

            self.display_surface.fill('black')

            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    main_game = Game()
    main_game.mapping()
    main_game.run()