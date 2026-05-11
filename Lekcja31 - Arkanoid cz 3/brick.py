import pygame
import copy

from setup import *


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()
        self.image_original = pygame.image.load(f"{IMAGE_PATH}/brick.png")
        self.rect = pygame.Rect(x, y, 96, 48)
        self.hp = hp

    def update_state(self):
        color_mask = 0
        if self.hp == 3:
            color_mask = (128, 0, 0)
        if self.hp == 2:
            color_mask = (0, 0, 128)
        if self.hp == 1:
            color_mask = (0, 128, 0)

        self.image = copy.deepcopy(self.image_original)
        self.image.fill(color_mask, special_flags=pygame.BLEND_ADD)
        