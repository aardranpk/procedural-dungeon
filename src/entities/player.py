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

        # Stats
        self.max_health = 100
        self.health = self.max_health
        self.strength = 10
        self.level = 1
        self.xp = 0

        # Attack
        self.attack_range = tile_size
        self.attack_damage = self.strength
        self.attack_cooldown = 30  # frames
        self.attack_timer = 0

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

        # Update position with map boundaries enforcement
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, self.map_width * self.tile_size - self.width))
        self.y = max(0, min(self.y, self.map_height * self.tile_size - self.height))
        self.rect.topleft = (self.x, self.y)

        # Update attack timer
        if self.attack_timer > 0:
            self.attack_timer -= 1

    def attack(self, enemies):
        """Perform melee attack on nearby enemies"""
        if self.attack_timer > 0:
            return
        self.attack_timer = self.attack_cooldown

        # Attack rect around player
        attack_rect = self.rect.inflate(self.attack_range, self.attack_range)
        for enemy in enemies:
            if attack_rect.colliderect(enemy.rect):
                enemy.take_damage(self.attack_damage)
                self.gain_xp(10)  # gain XP for hitting enemy

    def gain_xp(self, amount):
        before_xp = self.xp
        self.xp += amount
        print(f"XP: {before_xp} → {self.xp}")

        if self.xp >= 100:
            self.level += 1
            self.xp -= 100
            self.strength += 5
            self.max_health += 20
            self.health = self.max_health
            print(f"LEVEL UP! → Level {self.level}")

    def draw_health_bar(self, surface):
        bar_width = self.width
        bar_height = 5
        fill = int((self.health / self.max_health) * bar_width)
        border_rect = pygame.Rect(self.rect.x, self.rect.y - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y - 10, fill, bar_height)
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)
        pygame.draw.rect(surface, (255, 255, 255), border_rect, 1)

    def draw_xp_bar(self, surface):
        bar_width = self.width
        bar_height = 3
        fill = int((self.xp / 100) * bar_width)
        border_rect = pygame.Rect(self.rect.x, self.rect.y - 15, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y - 15, fill, bar_height)
        pygame.draw.rect(surface, (0, 0, 255), fill_rect)
        pygame.draw.rect(surface, (255, 255, 255), border_rect, 1)
