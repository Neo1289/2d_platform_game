###LIBRARIES
from libraries_and_settings import (pygame,
                                    sys,
                                    random)
###CONFIGURATIONS
from libraries_and_settings import (display_surface, maps, TILE_SIZE, WINDOW_HEIGHT,WINDOW_WIDTH,font)
from words_library import phrases

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
        self.transition_bool = True
        self.phrases = phrases

        self.collision_sprites = pygame.sprite.Group()
        self.all_sprites = allSpritesOffset()
        self.player = None

        self.inventory = {
            'potion': 1,
            'crystal ball': 1,
            'coin': 0,
            'keys': 0,
            'holy water': 0
        }

        self.game_objects = ['potion','crystall ball','coin']

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

    def enter_area_check(self,event):
        for name, area in self.area_group.items():
        ###check if the player pressed yes key to enter the area
            if area.rect.colliderect(self.player.rect) and self.key_down(event,"y"):
                self.transition_bool = True

        ###perform the actual transition between areas
        if self.transition_bool:
            self.mapping()
            self.transition_bool = False

    def rendering(self):
        self.text_surface = None
        ###determine the current area map to be loaded and print it
        for name, area in self.area_group.items():
            if area.rect.colliderect(self.player.rect):
                self.current_area = name
                self.text = f"You found a {name} press Y to enter"
                self.text_surface = font.render(self.text,True,"white")

        for obj in self.collision_sprites:
            if self.object_id(obj):
               self.text = f"{self.phrases["text_2"]}{obj.name}?"
               self.text_surface = font.render(self.text, True, "white")

        if self.text_surface:
            text_rect = self.text_surface.get_rect(center=(WINDOW_WIDTH // 3, WINDOW_HEIGHT // 4))
            self.display_surface.blit(self.text_surface, text_rect)

    def collect_resources(self,event):
        for obj in self.collision_sprites:
            if self.object_id(obj):
                if self.key_down(event, "y"):
                    self.inventory[random.choice(self.game_objects)]+= 1

                    obj.resources = 0

    def display_captions(self):
        time_sec = pygame.time.get_ticks() // 1000
        self.caption = (f"\u2665 {self.player.life}      "
                        f"\U0001F9EA {self.inventory['potion']}      "
                        f"\U0001F52E {self.inventory['crystal ball']}     "
                        f"\U0001F4B0 {self.inventory['coin']}       "
                        f"\U0001F5DD {self.inventory['keys']}       "
                        f"\u2697\ufe0f {self.inventory['holy water']}      "
                        )
        pygame.display.set_caption(self.caption)

    ################################
    ####REDUNDANT CODE REDUCTION####
    ################################
    def object_id(self,obj):
        if obj.rect.colliderect(self.player.rect) and hasattr(obj, "name") and not hasattr(obj,
                                                                                           "human") and obj.resources == 1:
            return True

    def key_down(self, event, key: str):
        if event.type == pygame.KEYDOWN and  getattr(pygame, f"K_{key}"):
            return True

    def run(self):
        while self.running:
            dt = self.clock.tick() / 100
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                self.enter_area_check(event)
                self.collect_resources(event)

            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.player.rect.center)
            self.rendering()
            self.display_captions()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    main_game = Game()
    main_game.run()