import pygame
from Direction import Direction
from setup import IMAGE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH
import copy
from Segment import Segment
from egg import Egg


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.orginal_image = pygame.image.load(f"{IMAGE_PATH}head.png")
        self.image = pygame.transform.rotate(self.orginal_image, 0)
        self.rect = self.image.get_rect(center = (12*32+16, 9*32+16))

        self.direction = Direction.UP
        self.new_direction = Direction.UP

        self.last_position = copy.deepcopy(self.rect)
        self.add_segment = False
        self.segments = []

    def change_direction(self, expected_direction):
        if abs(self.direction.value - expected_direction.value) != 2:
            self.new_direction = expected_direction
            
    def eat_apple(self):
        self.add_segment = True
        


    def update(self):
        self.direction = self.new_direction
        self.image = pygame.transform.rotate(self.orginal_image,self.direction.value*-90)

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

            new_segment.position = new_position # Błąd wcięć
            self.segments.append(new_segment)
            self.add_segment = False


        self.last_position = copy.deepcopy(self.rect)

        if self.direction == self.direction.UP:
            self.rect.move_ip(0,-32)
        elif self.direction == self.direction.DOWN:
            self.rect.move_ip(0,32)
        elif self.direction == self.direction.LEFT:
            self.rect.move_ip(-32,0)
        elif self.direction == self.direction.RIGHT:
            self.rect.move_ip(32,0)


    def draw_segments(self, screen):
        for segment in self.segments:
            screen.blit(segment.image,segment.position)

    def check_collisions(self):
        for segment in self.segments:
            if self.rect.topleft == segment.position.topleft:
                return True
        
        if self.rect.top < 0 or self.rect.top >= SCREEN_HEIGHT:
            return True
        if self.rect.left < 0 or self.rect.left >= SCREEN_WIDTH:
            return True
        
        return False
