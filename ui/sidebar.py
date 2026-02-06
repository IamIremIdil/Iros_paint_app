import pygame
from utils.constants import WIDTH, HEIGHT, SIDEBAR_WIDTH, TAB_WIDTH, BG_COLOR


class Sidebar:
    """Collapsible sidebar with settings controls"""

    def __init__(self):
        self.is_open = False

        # Colors
        self.bg_color = (60, 63, 68)  # Dark charcoal
        self.tab_color = (100, 181, 246)  # Light blue
        self.border_color = (40, 43, 48)
        self.text_color = (255, 255, 255)

        # Tab properties
        self.tab_height = 100

        # Font
        self.font = pygame.font.SysFont("Arial", 16)

        # Example settings (add more as needed)
        self.brush_opacity = 1.0  # 0.0 to 1.0
        self.show_grid = False
        self.symmetry_mode = False

    def toggle(self):
        """Open/close the sidebar"""
        self.is_open = not self.is_open

    def draw(self, surface):
        """Draw the sidebar and tab"""
        if self.is_open:
            self._draw_sidebar(surface)
        self._draw_tab(surface)

    def _draw_sidebar(self, surface):
        """Draw the sidebar content when open"""
        # Sidebar background
        sidebar_rect = pygame.Rect(
            WIDTH - SIDEBAR_WIDTH,
            0,
            SIDEBAR_WIDTH,
            HEIGHT
        )
        pygame.draw.rect(surface, self.bg_color, sidebar_rect)

        # Left border
        pygame.draw.line(surface, self.border_color,
                         (WIDTH - SIDEBAR_WIDTH, 0),
                         (WIDTH - SIDEBAR_WIDTH, HEIGHT), 3)

        # Title
        title = self.font.render("Settings", True, self.text_color)
        surface.blit(title, (WIDTH - SIDEBAR_WIDTH + 20, 20))

        # Draw settings controls
        self._draw_settings(surface)

    def _draw_tab(self, surface):
        """Draw the collapsible tab"""
        tab_y = (HEIGHT - self.tab_height) // 2

        # Determine tab position based on state
        if self.is_open:
            tab_x = WIDTH - SIDEBAR_WIDTH
            tab_width = TAB_WIDTH
        else:
            tab_x = WIDTH - TAB_WIDTH
            tab_width = TAB_WIDTH

        # Tab background
        tab_rect = pygame.Rect(tab_x, tab_y, tab_width, self.tab_height)
        pygame.draw.rect(surface, self.tab_color, tab_rect)
        pygame.draw.rect(surface, self.border_color, tab_rect, 2)

        # Arrow icon
        arrow_size = 10
        center_x = tab_rect.centerx
        center_y = tab_rect.centery

        if self.is_open:
            # Left-pointing arrow
            points = [
                (center_x + 5, center_y - arrow_size),
                (center_x - 5, center_y),
                (center_x + 5, center_y + arrow_size)
            ]
        else:
            # Right-pointing arrow
            points = [
                (center_x - 5, center_y - arrow_size),
                (center_x + 5, center_y),
                (center_x - 5, center_y + arrow_size)
            ]

        pygame.draw.polygon(surface, self.text_color, points)

    def _draw_settings(self, surface):
        """Draw settings controls inside sidebar"""
        y_offset = 60
        setting_spacing = 40

        # Example: Opacity slider
        opacity_text = self.font.render(f"Opacity: {int(self.brush_opacity * 100)}%",
                                        True, self.text_color)
        surface.blit(opacity_text, (WIDTH - SIDEBAR_WIDTH + 20, y_offset))

        # Example: Toggle button for grid
        grid_text = self.font.render(f"Show Grid: {'ON' if self.show_grid else 'OFF'}",
                                     True, self.text_color)
        surface.blit(grid_text, (WIDTH - SIDEBAR_WIDTH + 20, y_offset + setting_spacing))

        # Example: Symmetry mode
        symmetry_text = self.font.render(f"Symmetry: {'ON' if self.symmetry_mode else 'OFF'}",
                                         True, self.text_color)
        surface.blit(symmetry_text, (WIDTH - SIDEBAR_WIDTH + 20, y_offset + setting_spacing * 2))

    def handle_click(self, pos):
        """Handle mouse clicks on the sidebar"""
        tab_y = (HEIGHT - self.tab_height) // 2

        # Tab hitbox
        if self.is_open:
            # Tab is on left side of sidebar
            tab_rect = pygame.Rect(
                WIDTH - SIDEBAR_WIDTH,
                tab_y,
                TAB_WIDTH,
                self.tab_height
            )
        else:
            # Tab is at screen edge
            tab_rect = pygame.Rect(
                WIDTH - TAB_WIDTH,
                tab_y,
                TAB_WIDTH,
                self.tab_height
            )

        if tab_rect.collidepoint(pos):
            self.toggle()
            return True

        # Handle clicks on sidebar controls if open
        if self.is_open and WIDTH - SIDEBAR_WIDTH <= pos[0] <= WIDTH:
            return self._handle_sidebar_click(pos)

        return False

    def _handle_sidebar_click(self, pos):
        """Handle clicks on sidebar controls"""
        y_offset = 60
        setting_spacing = 40

        # Toggle grid setting
        grid_rect = pygame.Rect(
            WIDTH - SIDEBAR_WIDTH + 20,
            y_offset + setting_spacing,
            150, 25
        )

        if grid_rect.collidepoint(pos):
            self.show_grid = not self.show_grid
            return True

        # Toggle symmetry setting
        symmetry_rect = pygame.Rect(
            WIDTH - SIDEBAR_WIDTH + 20,
            y_offset + setting_spacing * 2,
            150, 25
        )

        if symmetry_rect.collidepoint(pos):
            self.symmetry_mode = not self.symmetry_mode
            return True

        return False

    def get_canvas_width(self):
        """Get available width for painting (accounts for sidebar)"""
        return WIDTH - (SIDEBAR_WIDTH if self.is_open else 0)

    def is_point_in_sidebar(self, pos):
        """Check if a point is inside the sidebar area"""
        if not self.is_open:
            return False
        return WIDTH - SIDEBAR_WIDTH <= pos[0] <= WIDTH