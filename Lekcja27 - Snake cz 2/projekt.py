import pygame
from setup import *
import random
from Apple import Apple
from Direction import Direction
from Snake import Snake

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

for i in range(25):
    for j in range(19):
        image = pygame.image.load(f"{IMAGE_PATH}background.png")
        mask = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        # mask = (0, 0, 255)

        image.fill(mask, special_flags = pygame.BLEND_ADD)
        background.blit(image, (i*32, j*32))
        # Jak wyliczyć koordynaty danego kafelka na podstawie zmiennych i oraz j?
        # Kafelek ma wymiary 32x32

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

apple = Apple()
apples = pygame.sprite.Group()
apples.add(apple)

snake = Snake()
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 200)

game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_active = False
            elif event.key == pygame.K_w:
                snake.change_direction(Direction.UP)
            elif event.key == pygame.K_s:
                snake.change_direction(Direction.DOWN)
            elif event.key == pygame.K_a:
                snake.change_direction(Direction.LEFT)
            elif event.key == pygame.K_d:
                snake.change_direction(Direction.RIGHT)
        elif event.type == pygame.QUIT:
            game_active = False

    screen.blit(background, (0, 0))

    for apple in apples:
        screen.blit(apple.image, apple.rect)

    screen.blit(snake.image, snake.rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()