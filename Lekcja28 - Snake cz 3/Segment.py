import pygame
import copy
from setup import IMAGE_PATH

class Segment(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}segment.png")
        self.position = pygame.Rect(-32, -32, 32, 32)
        self.last_position = None

    def move(self, new_position):
        self.last_position = copy.deepcopy(self.position)
        self.new_position = copy.deepcopy(new_position)