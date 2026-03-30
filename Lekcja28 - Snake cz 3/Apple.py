import pygame
import random

from setup import IMAGE_PATH

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}apple.png")
        self.rect = pygame.Rect(random.randint(0, 24)*32, random.randint(0, 18)*32, 32, 32)

