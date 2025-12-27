import pygame
import random

class Tile:
    def __init__(self, grid_x, grid_y, tile_size, tile_type="floor"):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.tile_size = tile_size
        self.tile_type = tile_type
        self.image = pygame.Surface((tile_size, tile_size))

        if tile_type == "floor":
            self.image.fill((80, 80, 80))  # lighter gray
        elif tile_type == "wall":
            self.image.fill((30, 30, 30))  # dark gray
        elif tile_type == "special":
            self.image.fill((200, 180, 50))  # yellowish for special tiles

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
                rnd = random.random()
                if rnd < 0.2:
                    tile_type = "wall"
                elif rnd < 0.22:
                    tile_type = "special"
                else:
                    tile_type = "floor"
                tile = Tile(x, y, self.tile_size, tile_type)
                self.tiles.append(tile)
