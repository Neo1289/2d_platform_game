###LIBRARIES
from libraries_and_settings import (pygame,
                                    sys)
###CONFIGURATIONS
from libraries_and_settings import (display_surface, maps, TILE_SIZE)

###SPRITES
from player import Player
from camera import allSpritesOffset
from sprites import GeneralSprite,AreaSprite

pygame.init()

class Game:
    def __init__(self):

        self.running = True
        self.display_surface = display_surface
        self.clock = pygame.time.Clock()

        self.maps = maps
        self.current_map = None
        self.current_area = "world"
        self.area_group = {}

        self.collision_sprites = pygame.sprite.Group()
        self.all_sprites = allSpritesOffset()

        self.player = None

    def mapping(self):

        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.area_group.clear()

        for name, map in self.maps.items():
            if name == self.current_area:
                self.current_map = map

        ###ground
        for x, y, image in self.current_map.get_layer_by_name('ground').tiles():
            GeneralSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites,True)

        ###objects
        for obj in self.current_map.get_layer_by_name('objects'):
            GeneralSprite((obj.x, obj.y), obj.image, (self.all_sprites,self.collision_sprites),None,obj.name,1)


        ###player
        for obj in self.current_map.get_layer_by_name('areas'):
            if obj.name == 'player_spawn':
                if self.player is None:
                    self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                else:
                    self.player.collision_rect.center = (obj.x, obj.y)
                    self.all_sprites.add(self.player)

            if obj.name not in ('bat', 'scheleton', 'wall', 'flame', 'dragon'):
                self.area_group[obj.name] = AreaSprite(obj.x, obj.y, obj.width, obj.height, self.all_sprites)

    def transition(self):
        for name, area in self.area_group.items():
            if area.rect.colliderect(self.player.rect):
                self.current_area = name
            print(self.current_area)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

            self.display_surface.fill('black')
            self.transition()
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    main_game = Game()
    main_game.mapping()
    main_game.run()