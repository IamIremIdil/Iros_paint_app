import pygame
import pygame.gfxdraw


def draw_rounded_rect(surface, color, rect, radius):
    x, y, w, h = rect

    pygame.gfxdraw.aacircle(surface, x + radius, y + radius, radius, color)
    pygame.gfxdraw.aacircle(surface, x + w - radius - 1, y + radius, radius, color)
    pygame.gfxdraw.aacircle(surface, x + radius, y + h - radius - 1, radius, color)
    pygame.gfxdraw.aacircle(surface, x + w - radius - 1, y + h - radius - 1, radius, color)

    pygame.gfxdraw.filled_circle(surface, x + radius, y + radius, radius, color)
    pygame.gfxdraw.filled_circle(surface, x + w - radius - 1, y + radius, radius, color)
    pygame.gfxdraw.filled_circle(surface, x + radius, y + h - radius - 1, radius, color)
    pygame.gfxdraw.filled_circle(surface, x + w - radius - 1, y + h - radius - 1, radius, color)

    pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
    pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))


def draw_painting(surface, painting):
    for color, pos, size in painting:
        pygame.draw.circle(surface, color, pos, size)


def draw_menu(surface, width, active_size, active_color):
    pygame.draw.rect(surface, "gray", [0, 0, width, 70])
    pygame.draw.line(surface, "black", (0, 70), (width, 70), 3)

    brushes = []
    sizes = [20, 15, 10, 5]
    for i, size in enumerate(sizes):
        rect = pygame.draw.rect(surface, "black", [10 + i * 60, 10, 50, 50])
        pygame.draw.circle(surface, "white", rect.center, size)
        if active_size == size:
            pygame.draw.rect(surface, "green", rect, 3)
        brushes.append(rect)

    pygame.draw.circle(surface, active_color, (400, 35), 30, 3)

    colors = [
        ((0, 0, 255), [width - 35, 10, 25, 25]),
        ((255, 0, 0), [width - 35, 35, 25, 25]),
        ((0, 255, 0), [width - 60, 10, 25, 25]),
        ((255, 255, 0), [width - 60, 35, 25, 25]),
        ((0, 255, 255), [width - 85, 10, 25, 25]),
        ((255, 0, 255), [width - 85, 35, 25, 25]),
        ((0, 0, 0), [width - 110, 10, 25, 25]),
        ((255, 255, 255), [width - 110, 35, 25, 25]),
    ]

    color_rects = []
    for color, rect in colors:
        color_rects.append((color, pygame.draw.rect(surface, color, rect)))

    # ---- SAVE & CLEAR ----
    font = pygame.font.SysFont("Arial", 18)

    save_rect = pygame.Rect(width - 290, 10, 80, 50)
    clear_rect = pygame.Rect(width - 200, 10, 80, 50)

    pygame.draw.rect(surface, (100, 255, 100), save_rect, border_radius=8)
    pygame.draw.rect(surface, (255, 100, 100), clear_rect, border_radius=8)

    surface.blit(font.render("SAVE", True, (0, 0, 0)), (save_rect.x + 18, save_rect.y + 15))
    surface.blit(font.render("CLEAR", True, (0, 0, 0)), (clear_rect.x + 12, clear_rect.y + 15))

    return brushes, color_rects, save_rect, clear_rect
