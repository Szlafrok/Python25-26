import pygame
from Direction import Direction
from setup import IMAGE_PATH
import copy
from Segment import Segment

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.original_image = pygame.image.load(f"{IMAGE_PATH}head.png")
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center = (12*32+16, 9*32+16))

        self.direction = Direction.UP
        self.new_direction = Direction.UP

        self.last_position = copy.deepcopy(self.rect)
        self.add_segment = False
        self.segments = []

    def change_direction(self, expected_direction):
        change_possible = True
        if self.direction == Direction.UP and expected_direction == Direction.DOWN:
            change_possible = False
        if self.direction == Direction.DOWN and expected_direction == Direction.UP:
            change_possible = False
        if self.direction == Direction.RIGHT and expected_direction == Direction.LEFT:
            change_possible = False
        if self.direction == Direction.LEFT and expected_direction == Direction.RIGHT:
            change_possible = False

        if change_possible:
            self.new_direction = expected_direction


        # Zadanie samodzielne (++):
        # Proszę napisać pozostałe dwa warunki wykluczające obrót

        # Zadanie dodatkowe (++):
        # Z użyciem funkcji abs() (wartość bezwzględna) proszę zwinąć 4 powstałe ify
        # do jednego warunku. Wskazówka: użyj cechy .value w enumie.

    def draw_segments(self, screen):
        for segment in self.segments:
            screen.blit(segment.image, segment.position)

    def eat_apple(self):
        self.add_segment = True

    def update(self):
        self.direction = self.new_direction
        self.image = pygame.transform.rotate(self.original_image, self.direction.value* -90)

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[0].move(self.last_position)
            else:
                self.segments[i].move(self.segments[i-1].last_position)

        if self.add_segment:
            print("OK")
            new_segment = Segment()
            new_position = None
            if self.segments: # False jeśli lista jest pusta, True w p.p
                new_position = copy.deepcopy(self.segments[-1].last_position)
            else:
                new_position = copy.deepcopy(self.last_position)
            new_segment.position = new_position
            self.segments.append(new_segment)
            self.add_segment = False
            print(len(self.segments))

        self.last_position = copy.deepcopy(self.rect)

        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
        elif self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
        elif self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)
        elif self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)