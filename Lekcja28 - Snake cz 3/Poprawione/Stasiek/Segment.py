import pygame
import copy

class Segment(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load('Lekcja28 - Snake cz 3/assets/segment.png')              
        self.pozycja = pygame.Rect(-32, -32, -32, -32)
        self.ostatnia_pozycja = None
    
    def ruch(self, nowa_pozycja):
        self.ostatnia_pozycja = copy.deepcopy(self.pozycja) 
        self.pozycja = copy.deepcopy(nowa_pozycja) # Było nowa_pozycja, a musi być pozycja