import pygame
from settings import TILE_SIZE, COLORS


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100

    def move(self, dx, dy, game_map):
        nx = self.x + dx
        ny = self.y + dy

        if game_map[nx][ny] == 0:
            self.x = nx
            self.y = ny

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            COLORS["player"],
            (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )
