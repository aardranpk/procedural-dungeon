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
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 2

        # Stats
        self.max_health = 30
        self.health = self.max_health

    def update(self, dungeon_tiles):
        dx, dy = random.choice([(self.speed,0), (-self.speed,0), (0,self.speed), (0,-self.speed), (0,0)])
        new_rect = self.rect.move(dx, dy)

        # Collision with walls
        for tile in dungeon_tiles:
            if tile.tile_type == "wall" and new_rect.colliderect(tile.rect):
                dx = dy = 0
                break

        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

    def take_damage(self, amount):
        self.health -= amount
        print(f"Enemy hit! HP now: {self.health}")
        if self.health <= 0:
            print("Enemy defeated!")