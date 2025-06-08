# ---------------------------
# importing libraries
# ---------------------------
import pygame
import sys
from os import path, walk, listdir
from os.path import join

# ---------------------------
# Configuration Parameters
# ---------------------------

WINDOW_WIDTH, WINDOW_HEIGHT = 1024 ,768
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))