import pygame
from setup import IMAGE_PATH

class Image(pygame.sprite.Sprite):
    def __init__(self, path: str):
        super().__init__()
        self.image = pygame.image.load(path)

class Element():
    def __init__(self, elem_type):
        self.selected = 0 # wybrany

        self.image_list = [] # lista obrazów

        for i in range(1, 4):
            path = f"{IMAGE_PATH}{elem_type}{i}.png"
            loaded_image = Image(path)
            self.image_list.append(loaded_image)

    def selectNext(self):
        self.selected += 1
        if self.selected > 2:
            self.selected = 0