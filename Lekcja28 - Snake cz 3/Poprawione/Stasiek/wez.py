import pygame
from kierunek import kierunek
from copy import deepcopy
from Segment import Segment

class Waz(pygame.sprite.Sprite):
   def __init__(self):
      self.org = pygame.image.load('Lekcja28 - Snake cz 3/assets/head.png')
      self.obraz = pygame.transform.rotate(self.org, 0)
      self.rect = self.obraz.get_rect(center=(400 , 304))
      self.kierunek = kierunek.GORA
      self.new = kierunek.GORA

      self.ost_pozycja = deepcopy(self.rect)
      self.dodaj_segment = False
      self.segmenty = []
      

   def zmiana_kierunku(self, wybrany_kierunek):
      czy_możliwe = True
      if self.kierunek == kierunek.GORA and wybrany_kierunek == kierunek.DOL:
         czy_możliwe = False
      if self.kierunek == kierunek.DOL and wybrany_kierunek == kierunek.GORA:
         czy_możliwe = False
      if self.kierunek == kierunek.PRAWO and wybrany_kierunek == kierunek.LEWO:
         czy_możliwe = False
      if self.kierunek == kierunek.LEWO and wybrany_kierunek == kierunek.PRAWO:
         czy_możliwe = False
      if czy_możliwe:
         self.new = wybrany_kierunek

   def rysuj(self, ekran):
      for segment in self.segmenty:
         ekran.blit(segment.obraz, segment.pozycja)
   
   def jesc_jobko(self):
      self.dodaj_segment = True


   def aktualizuj(self):
      self.kierunek = self.new
      self.obraz = pygame.transform.rotate(self.org, self.kierunek.value* -90)
      
      self.ost_pozycja = deepcopy(self.rect) # To musi być przed ruchem segmentów - pierwszy segment musi znać miejsce, gdzie wąż był w poprzednim ruchu, zanim tam pójdzie.

      for i in range(len(self.segmenty)):
         if i == 0:
            self.segmenty[0].ruch(self.ost_pozycja)
         else:
            self.segmenty[i].ruch(self.segmenty[i-1].ostatnia_pozycja )  # Zmienna w segmentach nazywa się "ostatnia_pozycja", nie "ost_pozycja"
         
      if self.dodaj_segment:
         nowy_segment = Segment()
         nowa_pozycja = None
         if self.segmenty:
            nowa_pozycja = deepcopy(self.segmenty[-1].ostatnia_pozycja) # Jak wyżej
         else:
            nowa_pozycja = deepcopy(self.ost_pozycja) 
         nowy_segment.pozycja = nowa_pozycja
         self.segmenty.append(nowy_segment)
         self.dodaj_segment = False




      if self.kierunek == kierunek.GORA:
         self.rect.move_ip(0,-32)
      elif self.kierunek == kierunek.DOL:
         self.rect.move_ip(0, 32)
      elif self.kierunek == kierunek.LEWO:
         self.rect.move_ip(-32, 0)
      elif self.kierunek == kierunek.PRAWO:
         self.rect.move_ip(32, 0)

   def sprawdz_kolizje(self) -> bool:
      for segment in self.segmenty:
         if self.rect.topleft == segment.pozycja.topleft:
            return True
      if self.rect.top < 0 or self.rect.top >= 608: # Brak odwołania do stałych - zmiana rozmiarów gry będzie utrudniona.
         return True
      if self.rect.left < 0 or self.rect.left >= 800:
         return True
      
      return False
           



