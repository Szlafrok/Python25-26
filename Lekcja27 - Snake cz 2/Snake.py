import pygame
from Direction import Direction
from setup import IMAGE_PATH

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.original_image = pygame.image.load(f"{IMAGE_PATH}head.png")
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center = (12*32+16, 9*32+16))

        self.direction = Direction.UP
        self.new_direction = Direction.UP

    def change_direction(self, expected_direction):
        change_possible = True
        if self.direction == Direction.UP and expected_direction == Direction.DOWN:
            change_possible = False
        if self.direction == Direction.DOWN and expected_direction == Direction.UP:
            change_possible = False
        
        # Zadanie samodzielne (++):
        # Proszę napisać pozostałe dwa warunki wykluczające obrót

        # Zadanie dodatkowe (++):
        # Z użyciem funkcji abs() (wartość bezwzględna) proszę zwinąć 4 powstałe ify
        # do jednego warunku