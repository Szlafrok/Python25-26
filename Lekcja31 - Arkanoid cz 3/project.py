import pygame

from setup import *
from pad import Pad
from ball import Ball
from brick import Brick

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

pad = Pad()
ball = Ball()

bg_image = pygame.image.load(f"{IMAGE_PATH}/background.png")

lives = LIVES # lives = 3
level = 0
font = pygame.font.SysFont('Consolas', 24) # System Font

bricks = pygame.sprite.Group()

def add_bricks():
    loaded_level = LEVEL_0

    for row in range(7):
        for column in range(10):
            brick_state = loaded_level[row][column]
            if brick_state != 0:
                brick = Brick(32 + column * 96, 32 + row * 48, brick_state)
                bricks.add(brick)

add_bricks()

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
    
    ball.update(pad, bricks) #
    bricks.update() # 
    pad.update() #

    if ball.lost:
        lives -= 1
        if lives <= 0:
            break
        ball.reset_position()
        pad.reset_position()


    screen.blit(bg_image, (0, 0))
    screen.blit(pad.image, pad.position)
    screen.blit(ball.image, ball.position)

    for brick in bricks:
        screen.blit(brick.image, brick.rect)

    text = font.render(f'Życia: {lives}', False, (255, 255, 255))
    screen.blit(text, (16, 16))

    pygame.display.flip()
    clock.tick(30)