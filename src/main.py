import pygame
from settings import *
from dungeon.generator import DungeonGenerator
from entities.player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Procedural Dungeon")
clock = pygame.time.Clock()

generator = DungeonGenerator(MAP_WIDTH, MAP_HEIGHT)
game_map, rooms = generator.generate()

player_x, player_y = rooms[0].center()
player = Player(player_x, player_y)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move(0, -1, game_map)
    if keys[pygame.K_s]:
        player.move(0, 1, game_map)
    if keys[pygame.K_a]:
        player.move(-1, 0, game_map)
    if keys[pygame.K_d]:
        player.move(1, 0, game_map)

    screen.fill((0, 0, 0))

    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            color = COLORS["floor"] if game_map[x][y] == 0 else COLORS["wall"]
            pygame.draw.rect(
                screen,
                color,
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )

    player.draw(screen)
    pygame.display.flip()

pygame.quit()
