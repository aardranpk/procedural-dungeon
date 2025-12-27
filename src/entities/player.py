import pygame

class Player:
    def __init__(self, grid_x, grid_y, tile_size):
        self.tile_size = tile_size
        self.x = grid_x * tile_size
        self.y = grid_y * tile_size
        self.width = tile_size
        self.height = tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 0, 0))  # red player
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 4  # pixels per frame

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Update rect for camera
        self.rect.topleft = (self.x, self.y)
