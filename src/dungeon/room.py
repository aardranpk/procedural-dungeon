class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def center(self):
        return self.x + self.w // 2, self.y + self.h // 2

    def intersects(self, other):
        return (
            self.x <= other.x + other.w and
            self.x + self.w >= other.x and
            self.y <= other.y + other.h and
            self.y + self.h >= other.y
        )
