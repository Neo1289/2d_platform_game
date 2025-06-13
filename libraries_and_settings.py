# ---------------------------
# importing libraries
# ---------------------------
import pygame
import sys
from os import path, walk, listdir
from os.path import join
import pymunk
from pytmx.util_pygame import load_pygame

# ---------------------------
# Configuration Parameters
# ---------------------------
WINDOW_WIDTH, WINDOW_HEIGHT = 1024 ,768
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TILE_SIZE = 32

# ---------------------------
# maps
# ---------------------------
maps = {}
for dirpath, dirnames, filenames in walk(path.join('resources', 'world')):
    for filename in filenames:
        if filename.lower().endswith('.tmx'):
            maps[(filename.split('.')[0])] = (load_pygame(path.join('resources','world',filename)))
