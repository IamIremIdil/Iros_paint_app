import pygame
import pygame.gfxdraw

# UI Colors
MENU_BG = (60, 63, 68)  # Dark charcoal
MENU_BORDER = (40, 43, 48)  # Darker charcoal
ACCENT_COLOR = (100, 181, 246)  # Light blue
ACTIVE_BORDER = (220, 220, 220)  # Green
BUTTON_SAVE = (76, 175, 80)  # Green
BUTTON_CLEAR = (244, 67, 54)  # Red
BUTTON_HOVER = (220, 220, 220)  # Light gray
TEXT_COLOR = (255, 255, 255)  # White


def draw_rounded_rect(surface, color, rect, radius=8, border_width=0, border_color=None):
    #Draw a rounded rectangle with optional border#
    x, y, w, h = rect

    # Draw filled rounded rectangle
    if border_width == 0:
        # Filled corners
        pygame.gfxdraw.filled_circle(surface, x + radius, y + radius, radius, color)
        pygame.gfxdraw.filled_circle(surface, x + w - radius - 1, y + radius, radius, color)
        pygame.gfxdraw.filled_circle(surface, x + radius, y + h - radius - 1, radius, color)
        pygame.gfxdraw.filled_circle(surface, x + w - radius - 1, y + h - radius - 1, radius, color)

        # Filled rectangles
        pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
        pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))

    # Anti-aliased outline
    if border_width > 0 and border_color:
        pygame.gfxdraw.aacircle(surface, x + radius, y + radius, radius, border_color)
        pygame.gfxdraw.aacircle(surface, x + w - radius - 1, y + radius, radius, border_color)
        pygame.gfxdraw.aacircle(surface, x + radius, y + h - radius - 1, radius, border_color)
        pygame.gfxdraw.aacircle(surface, x + w - radius - 1, y + h - radius - 1, radius, border_color)

        pygame.draw.rect(surface, border_color, rect, border_width, border_radius=radius)


def draw_button(surface, rect, color, text, font, hover_color=None):
    #Draw a modern button with text#
    # Draw button background
    draw_rounded_rect(surface, color, rect, radius=12)

    # Add subtle shadow effect
    shadow_rect = (rect[0] + 2, rect[1] + 2, rect[2], rect[3])
    shadow_color = tuple(max(0, c - 40) for c in color)

    # Render text
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    surface.blit(text_surface, text_rect)

    # Draw border for depth
    pygame.draw.rect(surface, shadow_color, rect, 2, border_radius=12)


def draw_painting(surface, painting):
    #Draw all the brush strokes#
    for color, pos, size in painting:
        pygame.draw.circle(surface, color, pos, size)


def draw_menu(surface, width, active_size, active_color):
    #Draw the top menu bar with all controls#
    menu_height = 70

    # Draw menu background
    pygame.draw.rect(surface, MENU_BG, [0, 0, width, menu_height])

    # Draw bottom border
    pygame.draw.line(surface, MENU_BORDER, (0, menu_height), (width, menu_height), 3)

    # --- BRUSH SIZES ---
    brushes = []
    sizes = [20, 15, 10, 5]
    x_start = 18.5

    for i, size in enumerate(sizes):
        x = x_start + i * 65
        rect_obj = pygame.Rect(x, 10, 55, 50)

        # Draw button background
        btn_color = (80, 83, 88) if active_size == size else (70, 73, 78)
        draw_rounded_rect(surface, btn_color, rect_obj, radius=10)

        # Draw brush preview circle
        pygame.draw.circle(surface, (255, 255, 255), rect_obj.center, size)

        # Draw active indicator
        if active_size == size:
            pygame.draw.rect(surface, ACTIVE_BORDER, rect_obj, 3, border_radius=10)

        brushes.append(rect_obj)

    # --- COLOR PREVIEW (Current Color) ---
    preview_x = x_start + 65 * 7.8 + 35
    # --- COLOR PREVIEW (Current Color) ---
    PREVIEW_SCALE = 0.60  # ← change this

    base_size = 50
    base_radius = 10
    base_border = 5

    size = int(base_size * PREVIEW_SCALE)
    radius = int(base_radius * PREVIEW_SCALE)
    border = max(1, int(base_border * PREVIEW_SCALE))

    preview_rect = pygame.Rect(preview_x, 42, size, size)

    draw_rounded_rect(surface, active_color, preview_rect, radius=radius)
    pygame.draw.rect(surface, (200, 200, 200), preview_rect, border, border_radius=radius)

    # --- COLOR PALETTE ---
    palette_colors = [
        (0, 0, 0),  # Black
        (255, 255, 255),  # White
        (244, 67, 54),    # Red
        (233, 30, 99),    # Pink
        (156, 39, 176),   # Purple
        (103, 58, 183),   # Deep Purple
        (63, 81, 181),    # Indigo
        (33, 150, 243),   # Blue
        (3, 169, 244),    # Light Blue
        (0, 188, 212),    # Cyan
        (0, 150, 136),    # Teal
        (76, 175, 80),    # Green
        (139, 195, 74),   # Light Green
        (205, 220, 57),   # Lime
        (255, 235, 59),   # Yellow
        (255, 193, 7),    # Amber
        (255, 152, 0),    # Orange
        (255, 87, 34),    # Deep Orange
    ]

    color_rects = []
    colors_per_row = 9
    color_size = 28
    color_spacing = 32
    color_start_x = width - (colors_per_row * color_spacing + 240)

    for i, color in enumerate(palette_colors):
        row = i // colors_per_row
        col = i % colors_per_row
        x = color_start_x + col * color_spacing
        y = 10 + row * color_spacing

        rect = pygame.Rect(x, y, color_size, color_size)

        # Draw color button
        draw_rounded_rect(surface, color, rect, radius=6)

        # Draw border
        border_color = ACTIVE_BORDER if color == active_color else (100, 100, 100)
        border_width = 3 if color == active_color else 1
        pygame.draw.rect(surface, border_color, rect, border_width, border_radius=6)

        color_rects.append((color, rect))

    # --- SAVE & CLEAR BUTTONS ---
    font = pygame.font.SysFont("Arial", 16, bold=True)

    button_width = 85
    button_height = 50
    button_spacing = 10
    buttons_x = width - (2 * button_width + button_spacing + 15)

    save_rect = pygame.Rect(buttons_x, 10, button_width, button_height)
    clear_rect = pygame.Rect(buttons_x + button_width + button_spacing, 10, button_width, button_height)

    draw_button(surface, save_rect, BUTTON_SAVE, "SAVE", font)
    draw_button(surface, clear_rect, BUTTON_CLEAR, "CLEAR", font)

    return brushes, color_rects, save_rect, clear_rect