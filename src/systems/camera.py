class Camera:
    def __init__(self, map_width, map_height, screen_width, screen_height, tile_size):
        self.tile_size = tile_size
        self.map_width = map_width
        self.map_height = map_height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 0  # camera top-left x
        self.y = 0  # camera top-left y

    def update(self, player_x, player_y):
        # Center camera on player
        self.x = player_x - self.screen_width // 2
        self.y = player_y - self.screen_height // 2

        # Clamp camera to map bounds
        self.x = max(0, min(self.x, self.map_width * self.tile_size - self.screen_width))
        self.y = max(0, min(self.y, self.map_height * self.tile_size - self.screen_height))

    def apply(self, rect):
        """Shift a rect by camera position before drawing"""
        return rect.move(-self.x, -self.y)
