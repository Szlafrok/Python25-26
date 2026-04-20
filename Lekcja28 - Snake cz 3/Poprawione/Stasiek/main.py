import pygame
import time
import random
from jablko import Jablko
from wez import Waz #  (・・?
from kierunek import kierunek

pygame.init()
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)  # 200 = 200 ms | 1000 ms = 1 sec


jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)              



#sze - szerokosc ekranu
#wys - wysokosc ekranu
sze = 800 
wys = 608

ekran = pygame.display.set_mode((sze, wys))
tlo = pygame.Surface((sze, wys))

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("Lekcja28 - Snake cz 3/assets/background.png")
        maska = (random.randint(0,20), random.randint(0,20), random.randint(0,20))
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))


zegar = pygame.time.Clock()
gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == PORUSZ_WEZEM:  
            waz.aktualizuj()
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN: 
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
                game_active = False
            elif zdarzenie.key == pygame.K_w:
                waz.zmiana_kierunku(kierunek.GORA)  # ??????????????????? HuuUUHHHH ?!?!? 
            elif zdarzenie.key == pygame.K_s: # Odpowiadając na pytanie - wywołujesz metodę z określonym kierunkiem. Potem wąż na podstawie
                waz.zmiana_kierunku(kierunek.DOL) # podanego przez Ciebie kierunku ustawia sobie odpowiednią rotację.
            elif zdarzenie.key == pygame.K_a:
                waz.zmiana_kierunku(kierunek.LEWO)
            elif zdarzenie.key == pygame.K_d:
                waz.zmiana_kierunku(kierunek.PRAWO)
    
    collizja_jobko = pygame.sprite.spritecollideany(waz, jablka)
    if collizja_jobko != None:
        collizja_jobko.kill() # Brak nawiasów. Poza tym przywracasz potem to samo jabłko, a musisz utworzyć nowe.
        waz.jesc_jobko() # Brak nawiasów.
        jablko = Jablko()
        jablka.add(jablko)

    
    
    
    
    ekran.blit(tlo, (0,0)) 
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)
    ekran.blit(waz.obraz, waz.rect)

    waz.rysuj(ekran) # Brakło Ci wywołania tej metody

    if waz.sprawdz_kolizje(): gra_dziala = False # brakowało sprawdzenia kolizji

    zegar.tick(30)
    pygame.display.flip()  #pygame.display.update()

time.sleep(0.1)
pygame.quit()   