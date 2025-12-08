import pygame
pygame.init()

SCREEN_WIDTH = 800 # Szerokość
SCREEN_HEIGHT = 600 # Wysokość

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption("Pierwsza gra")

game_status = True



liczenie = 0
while game_status:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
        elif event.type == pygame.KEYDOWN:
            if 

    pygame.display.update()
    print(liczenie)

pygame.quit()