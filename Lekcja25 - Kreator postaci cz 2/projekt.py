import pygame
import Element

from setup import SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_PATH

bg_image = pygame.image.load(f"{IMAGE_PATH}background.png")
character_image = pygame.image.load(f"{IMAGE_PATH}base.png")
character_hat = Element.Hat() # Proszę uzupełnić pozostałe obiekty

pygame.init()

ekran = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

game_active = True 

while game_active:
    # Obsługa zdarzeń / Event handling
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                game_active = False
        elif zdarzenie.type == pygame.QUIT:
            game_active = False

    ekran.blit(bg_image, (0, 0))
    ekran.blit(character_image, (270, 130))
    pygame.display.flip()
    clock.tick(60)

print("Opuszczono grę")
pygame.quit()