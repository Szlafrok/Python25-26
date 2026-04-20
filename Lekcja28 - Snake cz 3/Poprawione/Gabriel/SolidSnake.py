import pygame
from spokoloco import Direction
from putes import IMAGE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH
import copy
from Segment import Segment

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.orginal_image = pygame.image.load(f"{IMAGE_PATH}head.png")
        self.image = pygame.transform.rotate(self.orginal_image, 0)
        self.rect = self.image.get_rect(center = (12*32+16, 9*32+16))

        self.direction = Direction.UP
        self.new_direction = Direction.UP

        self.last_position = copy.deepcopy(self.rect)
        self.add_segment = False # Tu było "s" na końcu - literówka, która psuła działanie
        self.segments = []

    def change_Direction(self, expected_direction):
        change_possible = True
        if self.direction == Direction.UP and expected_direction == Direction.DOWN:
            change_possible = False
        if self.direction == Direction.DOWN and expected_direction == Direction.UP:
            change_possible = False
        if self.direction == Direction.LEFT and expected_direction == Direction.RIGHT:
            change_possible = False
        if self.direction == Direction.RIGHT and expected_direction == Direction.LEFT:
            change_possible = False

        if change_possible:
            self.new_direction = expected_direction

    def draw_segments(self, screen):
        for segment in self.segments:
            screen.blit(segment.image, segment.position)

    def eat_apple(self):
        self.add_segment = True

    def update(self):
        self.direction = self.new_direction
        self.image = pygame.transform.rotate(self.orginal_image, self.direction.value* -90)
        self.last_position = copy.deepcopy(self.rect) # błąd z zajęć - pierwszy segment musi korzystać z aktualnego śladu po wężu

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[0].move(self.last_position)
            else:
                self.segments[i].move(self.segments[i-1].last_position)
        
        if self.add_segment:
            new_segment = Segment()
            new_position = None
            if self.segments:
                new_position = copy.deepcopy(self.segments[-1].last_position)
            else:
                new_position = copy.deepcopy(self.last_position)
            new_segment.position = new_position # To powinno być poza if/else: dodajemy segment niezaleznie, czy to pierwszy, czy kolejny
            self.segments.append(new_segment) # Brakowało linijki z dodawaniem segmentu do listy - trzeba go przechować!
            self.add_segment = False


        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
        elif self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
        elif self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)
        elif self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)

    def check_collisions(self) -> bool:
        for segment in self.segments:
            if self.rect.topleft == segment.position.topleft:
                return True
        
        if self.rect.top < 0 or self.rect.top >= SCREEN_HEIGHT:
            return True
        if self.rect.top < 0 or self.rect.top >= SCREEN_WIDTH:
            return True
        
        return False