import random
from dungeon.room import Room


class DungeonGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[1 for _ in range(height)] for _ in range(width)]
        self.rooms = []

    def carve_room(self, room):
        for x in range(room.x, room.x + room.w):
            for y in range(room.y, room.y + room.h):
                self.map[x][y] = 0

    def h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y] = 0

    def v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y] = 0

    def carve_tunnel(self, x1, y1, x2, y2):
        if random.choice([True, False]):
            self.h_tunnel(x1, x2, y1)
            self.v_tunnel(y1, y2, x2)
        else:
            self.v_tunnel(y1, y2, x1)
            self.h_tunnel(x1, x2, y2)

    def generate(self, max_rooms=10):
        for _ in range(max_rooms):
            w = random.randint(5, 10)
            h = random.randint(5, 10)
            x = random.randint(1, self.width - w - 1)
            y = random.randint(1, self.height - h - 1)

            new_room = Room(x, y, w, h)

            if any(new_room.intersects(r) for r in self.rooms):
                continue

            self.carve_room(new_room)

            if self.rooms:
                prev_x, prev_y = self.rooms[-1].center()
                new_x, new_y = new_room.center()
                self.carve_tunnel(prev_x, prev_y, new_x, new_y)

            self.rooms.append(new_room)

        return self.map, self.rooms
