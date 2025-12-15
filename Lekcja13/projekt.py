def load_image(img_path, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center = position)

    return [image, surface, rect]

def print_image(img_data):
    _, surface, rect = img_data
    screen_surface.blit(surface, rect)
    return

import pygame
pygame.init()

SCREEN_WIDTH = 800 # Szerokość
SCREEN_HEIGHT = 600 # Wysokość

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pierwsza gra")

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image("Lekcja13/assets/player.png", player_pos)

game_status = True

clock = pygame.time.Clock()

#liczenie = 0
while game_status:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game_status = False

    print_image(player)

    pygame.display.update()
    #print(liczenie)
    clock.tick(60)
    
print("Zamykanie aplikacji...")
pygame.quit()