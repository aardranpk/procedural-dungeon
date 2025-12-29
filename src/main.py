import pygame
import random
from dungeon.generator import Dungeon
from entities.player import Player
from entities.enemy import Enemy
from entities.item import Item
from systems.camera import Camera

# Screen and map setup
screen_width = 800
screen_height = 600
tile_size = 32
map_width = 50
map_height = 50

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Procedural Dungeon Crawler v1.3.0")
clock = pygame.time.Clock()
FPS = 60

# Game objects
dungeon = Dungeon(map_width, map_height, tile_size)
player = Player(5, 5, tile_size, map_width, map_height)

# Multiple enemies
enemies = [
    Enemy(10, 10, tile_size),
    Enemy(15, 12, tile_size),
    Enemy(20, 18, tile_size)
]

# Items
items = []

for _ in range(8):  # 8 coins
    x = random.randint(2, map_width - 3)
    y = random.randint(2, map_height - 3)
    items.append(Item(x, y, tile_size, "coin"))

for _ in range(3):  # 3 potions
    x = random.randint(2, map_width - 3)
    y = random.randint(2, map_height - 3)
    items.append(Item(x, y, tile_size, "potion"))


camera = Camera(map_width, map_height, screen_width, screen_height, tile_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attack(enemies)

    # Update
    player.update(dungeon.tiles)
    for enemy in enemies[:]:
        enemy.update(dungeon.tiles)
        if enemy.health <= 0:
            enemies.remove(enemy)

    # Player-item collision
    for item in items[:]:
        if player.rect.colliderect(item.rect):
            item.apply_effect(player)
            items.remove(item)

    camera.update(player.x, player.y)

    # Draw
    screen.fill((0, 0, 0))
    for tile in dungeon.tiles:
        screen.blit(tile.image, camera.apply(tile.rect))

    for item in items:
        screen.blit(item.image, camera.apply(item.rect))

    for enemy in enemies:
        screen.blit(enemy.image, camera.apply(enemy.rect))

    screen.blit(player.image, camera.apply(player.rect))
    player.draw_health_bar(screen)
    player.draw_xp_bar(screen)

    hud_text = f"HP: {player.health}/{player.max_health}  |  LVL: {player.level}  |  XP: {player.xp}/100"
    hud_surface = font.render(hud_text, True, (255, 255, 255))
    screen.blit(hud_surface, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
