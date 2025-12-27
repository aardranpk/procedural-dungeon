import pygame
from dungeon.generator import Dungeon
from entities.player import Player
from systems.camera import Camera

# ------------------------
# Screen and map settings
# ------------------------
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

# ------------------------
# Create game objects
# ------------------------
dungeon = Dungeon(map_width, map_height, tile_size)
player = Player(5, 5, tile_size)

# Initialize camera
camera = Camera(map_width, map_height, screen_width, screen_height, tile_size)

# ------------------------
# Main game loop
# ------------------------
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ------------------------
    # Update game logic
    # ------------------------
    player.update()                     # update player movement
    camera.update(player.x, player.y)   # update camera to follow player

    # ------------------------
    # Draw everything
    # ------------------------
    screen.fill((0, 0, 0))  # clear screen

    # Draw dungeon tiles
    for tile in dungeon.tiles:
        screen_rect = camera.apply(tile.rect)
        screen.blit(tile.image, screen_rect)

    # Draw player
    screen_rect = camera.apply(player.rect)
    screen.blit(player.image, screen_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
