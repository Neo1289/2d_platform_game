from libraries_and_settings import pygame,random

class GeneralSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, ground_att: bool, name: str= None, resources: int= 0, item: bool= None):
         super().__init__(groups)

         self.resources = 10 if name == 'spawning chest' else resources
         if ground_att: self.ground = True
         self.image = surf
         self.rect = self.image.get_rect(topleft = pos)
         if item : self.item = item
         #determine the enemy attribute
         if name:
              self.name = name
              if self.name in ('merchant'): self.human = True
              if self.name == 'runes' : self.rune = True
         if name:
              if self.name == 'spawning chest': ###add the names of all the objects that have to move
                    self.temp = True
                    self.spawn_timer = 0
                    self.spawn_cooldown = 3

    def update(self,dt):
        try:
            if self.temp:
                self.spawn_timer += dt
                if self.spawn_timer >= self.spawn_cooldown:
                    new_x = random.randint(660, 880)
                    new_y = random.randint(700, 1000)
                    self.rect.center = (new_x, new_y)
                    self.spawn_timer = 0
        except:
            pass

#######################
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width,height,groups,name=None):
        super().__init__(groups)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)
        if name == 'danger area': self.dangerous = True

#######################
class NPC(pygame.sprite.Sprite):
    def __init__(self,pos,frames,groups,name: str,speed: int,dangerous: bool, direction: list = None, follow_player: bool = False):
        super().__init__(groups)

        self.frames, self.frames_index = frames,0
        self.image = self.frames[self.frames_index]
        self.animation_speed = 10

        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.Vector2(pos)
        self.list = direction
        self.direction = pygame.Vector2(random.choice(self.list), random.choice(self.list))
        self.speed = speed
        if dangerous: self.dangerous = dangerous
        self.name = name
        self.follow_player = follow_player
        self.player = None

    def animate(self, dt):
            self.frames_index += self.animation_speed * dt
            self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def move(self, dt):
        if self.follow_player and self.player:
            player_pos = pygame.Vector2(self.player.rect.center)
            self.direction = (player_pos - self.pos).normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.animate(dt)
        self.move(dt)
        if self.rect.center > (3000,3000) or self.rect.center < (-3000,-3000) :
            self.kill()