import pygame
import random
from setup import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}/ball.png")
        self.reset_position()
        self.r = 16
        self.lost = False


    def reset_position(self):
        self.coordinates = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120)
        self.position = self.image.get_rect(center = self.coordinates)

        self.vector = pygame.math.Vector2(0, -10)
        self.angle = random.randint(-30, 30)
        self.vector.rotate_ip(self.angle)

        self.lost = False


    def update(self, pad):
        self.coordinates += self.vector
        self.position.center = self.coordinates
        self.check_collisions(pad)

    def check_collisions(self, pad):
        # ZAMIAST rect MA BYĆ position
        # Ściany
        if self.position.left <= 0 or self.position.right >= SCREEN_WIDTH:
            self.vector.x *= -1
        if self.position.top <= 0:
            self.vector.y *= -1
        if self.position.bottom >= SCREEN_HEIGHT:
            self.lost = True

        # platforma
        if self.position.colliderect(pad.position):
            self.vector.y *= -1
            self.vector.x += pad.is_moving * 5
            if self.vector.x < -10: self.vector.x = -10
            if self.vector.x > 10: self.vector.x = 10