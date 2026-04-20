import random
import pygame
from setup import IMAGE_PATH

class Egg(pygame.sprite.Sprite): # Widzę że jest zaczęte, ale niedokończone :P
    def __init__(self):
        super(Egg, self).__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}egg.png")
        self.rect = pygame.Rect(random.randint(0, 24)*32, random.randint(0, 18)*32, 32, 32)