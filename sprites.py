from libraries_and_settings import pygame

class GeneralSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, ground_att: bool, name: str = None, resources: int = 0):
         super().__init__(groups)
         self.image = surf
         self.rect = self.image.get_rect(topleft = pos)
         if name: self.name = name
         self.resources = resources
         if ground_att: self.ground = True