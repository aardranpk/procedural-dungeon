import pygame

class Item:
    def __init__(self, x, y, tile_size, type="coin"):
        self.rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
        self.type = type
        self.image = pygame.Surface((tile_size, tile_size))
        if type == "coin":
            self.image.fill((255, 215, 0))
        elif type == "potion":
            self.image.fill((0, 255, 0))

    def apply_effect(self, player):
        if self.type == "coin":
            print("Picked up COIN → +5 XP")
            player.gain_xp(5)

        elif self.type == "potion":
            before = player.health
            player.health = min(player.max_health, player.health + 30)
            print(f"Picked up POTION → HP {before} → {player.health}")