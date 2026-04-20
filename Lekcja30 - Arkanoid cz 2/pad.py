import pygame

from setup import *


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}/pad.png")
        self.is_moving = 0
        self.reset_position()

    def update(self):
        self.is_moving = 0

    def reset_position(self):
        self.position = pygame.Rect(SCREEN_WIDTH / 2 - 70, SCREEN_HEIGHT - 80, 140, 30)

    def move_pad(self, value):
        speed = 10
        self.is_moving = value
        self.position.move_ip(value * speed, 0)
        if self.position.left <= 0: self.position.x = 0
        if self.position.right >= SCREEN_WIDTH: self.position.x = SCREEN_WIDTH - self.position.width