import math


class Brush:
    ## Represents the painting brush with color, size, and stroke history

    # Default values
    DEFAULT_SIZE = 15
    DEFAULT_COLOR = (0, 0, 0)  # Black

    def __init__(self, size=None, color=None):
        ### Initialize brush with optional size and color
        self.size = size or self.DEFAULT_SIZE
        self.color = color or self.DEFAULT_COLOR
        self.painting = []  # List of (color, position, size) tuples
        self._menu_rects = None  # Cache menu rectangles
        self.last_pos = None  # Store last mouse position for smooth drawing

    def paint(self, pos):
        ### Add a brush stroke at the given position with smooth lines
        if self.size <= 0:
            return

        # If this is the first point
        if self.last_pos is None:
            self.painting.append((self.color, pos, self.size))
            self.last_pos = pos
            return

        # Get the last point in painting
        x1, y1 = self.last_pos
        x2, y2 = pos

        # Calculate distance
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance > 0:
            # We draw a point every 2 pixels for maximum smoothness
            # instead of relying on the brush size.
            steps = max(1, int(distance / 2))
            for i in range(1, steps + 1):
                t = i / steps
                curr_x = int(x1 + (x2 - x1) * t)
                curr_y = int(y1 + (y2 - y1) * t)
                self.painting.append((self.color, (curr_x, curr_y), self.size))

        self.last_pos = pos

        if distance == 0:
            return

        # Determine number of points to draw
        if distance < self.size * 0.5:
            # Points are very close, just add one
            self.painting.append((self.color, pos, self.size))
        else:
            # Draw interpolated points
            steps = max(2, int(distance / (self.size * 0.7)))
            for i in range(steps + 1):
                t = i / steps
                x = int(x1 * (1 - t) + x2 * t)
                y = int(y1 * (1 - t) + y2 * t)
                self.painting.append((self.color, (x, y), self.size))

        self.last_pos = pos

    def clear(self):
        ###Clear all strokes from the canvas
        self.painting = []
        self.last_pos = None  # Reset last position when clearing

    def undo(self, steps=1):
        ###Remove the last N strokes
        if self.painting:
            self.painting = self.painting[:-steps]
        # Reset last_pos since stroke history changed
        self.last_pos = None

    def set_menu_rects(self, rects):
        ###Cache the menu rectangles for click detection
        self._menu_rects = rects

    def get_menu_rects(self):
        ###Get cached menu rectangles
        return self._menu_rects if self._menu_rects else ([], [], None, None)

    def get_stroke_count(self):
        ###Get the total number of strokes
        return len(self.painting)

    def __repr__(self):
        ###String representation for debugging
        return f"Brush(size={self.size}, color={self.color}, strokes={len(self.painting)})"