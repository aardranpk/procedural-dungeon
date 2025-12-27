import pygame

class Player:
    def __init__(self, grid_x, grid_y, tile_size, map_width, map_height):
        self.tile_size = tile_size
        self.map_width = map_width
        self.map_height = map_height
        self.x = grid_x * tile_size
        self.y = grid_y * tile_size
        self.width = tile_size
        self.height = tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 4
        self.max_health = 100
        self.health = self.max_health

    def update(self, dungeon_tiles):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        # Tentative new position
        new_rect = self.rect.move(dx, dy)

        # Collision detection with wall tiles
        for tile in dungeon_tiles:
            if tile.tile_type == "wall" and new_rect.colliderect(tile.rect):
                dx = dy = 0
                break

        # Update position with boundaries enforcement
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, self.map_width * self.tile_size - self.width))
        self.y = max(0, min(self.y, self.map_height * self.tile_size - self.height))

        self.rect.topleft = (self.x, self.y)

    def draw_health_bar(self, surface):
        # Draw above the player
        bar_width = self.width
        bar_height = 5
        fill = int((self.health / self.max_health) * bar_width)
        border_rect = pygame.Rect(self.rect.x, self.rect.y - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y - 10, fill, bar_height)
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)       # health fill
        pygame.draw.rect(surface, (255, 255, 255), border_rect, 1)  # border
