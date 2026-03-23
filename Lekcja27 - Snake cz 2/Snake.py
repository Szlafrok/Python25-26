import pygame
from Direction import Direction
from setup import IMAGE_PATH

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.original_image = pygame.image.load(f"{IMAGE_PATH}head.png")