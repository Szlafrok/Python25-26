import pygame

from setup import *
from pad import Pad
from ball import Ball

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

pad = Pad()
ball = Ball()

bg_image = pygame.image.load(f"{IMAGE_PATH}/background.png")

lives = LIVES # lives = 3
font = pygame.font.SysFont('Consolas', 24) # System Font

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
    
    ball.update(pad)
    pad.update()

    if ball.lost:
        lives -= 1
        if lives <= 0:
            break
        ball.reset_position()
        pad.reset_position()


    screen.blit(bg_image, (0, 0))
    screen.blit(pad.image, pad.position)
    screen.blit(ball.image, ball.position)

    text = font.render(f'Życia: {lives}', False, (255, 255, 255))
    screen.blit(text, (16, 16))

    pygame.display.flip()
    clock.tick(30)