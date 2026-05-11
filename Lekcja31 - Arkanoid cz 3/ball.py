import pygame
import random
from setup import *
from brick import Brick

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


    def update(self, pad, bricks):
        self.coordinates += self.vector
        self.position.center = self.coordinates
        self.check_collisions(pad, bricks)

    def check_collisions(self, pad, bricks):
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

        # klocki
        for brick in bricks:
            if self.brick_collision(brick): # poprawka
                brick.hit()
                break
        
    def brick_collision(self, brick: Brick):
        distance_x = abs(self.position.centerx - brick.rect.centerx) - brick.rect.width / 2
        distance_y = abs(self.position.centery - brick.rect.centery) - brick.rect.height / 2

        if distance_x < self.r and distance_y < self.r:
            if distance_y > distance_x:
                self.vector.y *= -1
            else:
                self.vector.x *= -1
            return True
        return False