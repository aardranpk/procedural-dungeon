import pygame
import random

class Enemy:
    def __init__(self, grid_x, grid_y, tile_size):
        self.tile_size = tile_size
        self.x = grid_x * tile_size
        self.y = grid_y * tile_size
        self.width = tile_size
        self.height = tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((0, 0, 255))  # blue enemy
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 2

    def update(self, dungeon_tiles):
        # Random movement
        dx, dy = random.choice([(self.speed,0), (-self.speed,0), (0,self.speed), (0,-self.speed), (0,0)])
        new_rect = self.rect.move(dx, dy)

        # Collision with walls
        for tile in dungeon_tiles:
            if tile.image.get_at((0, 0)) == (30, 30, 30, 255) and new_rect.colliderect(tile.rect):
                dx = dy = 0
                break

        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)
