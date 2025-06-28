from libraries_and_settings import pygame

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
              if self.name in ('bat', 'scheleton', 'wall', 'flame', 'dragon'): self.enemy = True
              if self.name in ('merchant'): self.human = True
              if self.name not in ('bat', 'scheleton', 'wall', 'flame', 'dragon','merchant'): self.item = True
              if self.name == 'runes' : self.rune = True

class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width,height,groups):
        super().__init__(groups)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)
