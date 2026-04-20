import pygame
import random

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("Lekcja28 - Snake cz 3/assets/apple.png")
        self.rect = pygame.Rect(random.randint(0,24) * 32, random.randint(0,18) * 32, 32, 32)