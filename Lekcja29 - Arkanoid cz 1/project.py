import pygame

from setup import *

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

bg_image = pygame.image.load(f"{IMAGE_PATH}/background.png")


# main loop
game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_active = False
        elif event.type == pygame.QUIT:
            game_active = False

    
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()
    clock.tick(30)