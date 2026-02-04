class Brush:
    def __init__(self):
        self.size = 0
        self.color = "white"
        self.painting = []

    def paint(self, pos):
        if self.size > 0:
            self.painting.append((self.color, pos, self.size))

    def clear(self):
        self.painting = []
