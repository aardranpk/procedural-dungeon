import pygame
import random

class Tile:
    def __init__(self, grid_x, grid_y, tile_size):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.tile_size = tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((50, 50, 50))  # gray for floor
        self.rect = pygame.Rect(grid_x * tile_size, grid_y * tile_size, tile_size, tile_size)

class Dungeon:
    def __init__(self, map_width, map_height, tile_size):
        self.map_width = map_width
        self.map_height = map_height
        self.tile_size = tile_size
        self.tiles = []
        self.generate_dungeon()

    def generate_dungeon(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                # Simple random dungeon: 80% floor, 20% wall
                tile = Tile(x, y, self.tile_size)
                if random.random() < 0.2:
                    tile.image.fill((30, 30, 30))  # darker for walls
                self.tiles.append(tile)
