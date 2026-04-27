import pygame

from setup import *
from pad import Pad


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

pad = Pad()


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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pad.move_pad(-1)
    if keys[pygame.K_d]:
        pad.move_pad(1)
    
    screen.blit(bg_image, (0, 0))
    screen.blit(pad.image, pad.position)
    pygame.display.flip()
    clock.tick(30)