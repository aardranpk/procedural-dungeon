import pygame
from dungeon.generator import Dungeon
from entities.player import Player
from entities.enemy import Enemy
from systems.camera import Camera

# Screen and map setup
screen_width = 800
screen_height = 600
tile_size = 32
map_width = 50
map_height = 50

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Procedural Dungeon Crawler")
clock = pygame.time.Clock()
FPS = 60

# Game objects
dungeon = Dungeon(map_width, map_height, tile_size)
player = Player(5, 5, tile_size, map_width, map_height)
enemy = Enemy(10, 10, tile_size)

camera = Camera(map_width, map_height, screen_width, screen_height, tile_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic
    player.update(dungeon.tiles)
    enemy.update(dungeon.tiles)
    camera.update(player.x, player.y)

    # Draw
    screen.fill((0, 0, 0))
    for tile in dungeon.tiles:
        screen_rect = camera.apply(tile.rect)
        screen.blit(tile.image, screen_rect)

    screen.blit(enemy.image, camera.apply(enemy.rect))
    screen.blit(player.image, camera.apply(player.rect))
    player.draw_health_bar(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
