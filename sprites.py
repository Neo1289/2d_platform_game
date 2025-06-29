from libraries_and_settings import pygame,random

class GeneralSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, ground_att: bool, name: str=None, resources: int = 0):
         super().__init__(groups)

         self.resources = resources
         if ground_att: self.ground = True
         self.image = surf
         self.rect = self.image.get_rect(topleft = pos)
         #determine the enemy attribute
         if name:
              self.name = name
              if self.name in ('merchant'): self.human = True
              if self.name not in ('bat', 'scheleton', 'wall', 'flame', 'dragon','merchant'): self.item = True
              if self.name == 'runes' : self.rune = True

#######################
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width,height,groups):
        super().__init__(groups)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)

#######################
class NPC(pygame.sprite.Sprite):
    def __init__(self,pos,frames,groups,name: str,speed: int,dangerous: bool):
        super().__init__(groups)

        self.frames, self.frames_index = frames,0
        self.image = self.frames[self.frames_index]
        self.animation_speed = 10

        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.Vector2(pos)
        self.list = [-1,1]
        self.direction = pygame.Vector2(random.choice(self.list), random.choice(self.list))
        self.speed = speed
        if dangerous: self.dangerous = dangerous
        self.name = name

    def animate(self, dt):
        self.frames_index += self.animation_speed * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def move(self, dt):
        if self.name != 'flame':
            self.pos += self.direction * self.speed * dt
            self.rect.center = self.pos
        else:
            pass

    def update(self, dt):
        self.animate(dt)
        self.move(dt)
        if self.rect.center > (3000,3000) or self.rect.center < (-3000,-3000) :
            self.kill()