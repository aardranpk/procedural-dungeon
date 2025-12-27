class Camera:
    def __init__(self, map_width, map_height, screen_width, screen_height, tile_size):
        self.tile_size = tile_size
        self.map_width = map_width
        self.map_height = map_height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 0
        self.y = 0

    def update(self, player_x, player_y):
        # Smooth camera using linear interpolation (lerp)
        lerp_factor = 0.1
        target_x = player_x - self.screen_width // 2
        target_y = player_y - self.screen_height // 2
        self.x += (target_x - self.x) * lerp_factor
        self.y += (target_y - self.y) * lerp_factor

        # Clamp to map boundaries
        self.x = max(0, min(self.x, self.map_width * self.tile_size - self.screen_width))
        self.y = max(0, min(self.y, self.map_height * self.tile_size - self.screen_height))

    def apply(self, rect):
        return rect.move(-self.x, -self.y)
