import pygame
from pathlib import Path

from ui.canvas import draw_menu, draw_painting
from tools.brush import Brush

def asset_path(*parts):
    return str(BASE_DIR.joinpath("assets", *parts))


pygame.init()
pygame.mixer.init()

BASE_DIR = Path(__file__).resolve().parent
SOUND_PATH = BASE_DIR / "assets" / "sounds" / "select_sound.ogg"
select_sound = pygame.mixer.Sound(asset_path("sounds", "select_sound.ogg"))

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Iro's paint app")

clock = pygame.time.Clock()
brush = Brush()



def save_painting(painting):
    surface = pygame.Surface((WIDTH, HEIGHT - 70))
    surface.fill((255, 255, 255))

    for color, pos, size in painting:
        pygame.draw.circle(surface, color, (pos[0], pos[1] - 70), size)

    pygame.image.save(surface, "painting.png")


run = True
while run:
    clock.tick(120)
    screen.fill("white")

    mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] and mouse[1] > 70:
        brush.paint(mouse)

    draw_painting(screen, brush.painting)
    if mouse[1] > 70:
        pygame.draw.circle(screen, brush.color, mouse, brush.size)

    brushes, colors, save_button, clear_button = draw_menu(screen, WIDTH, brush.size, brush.color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(brushes):
                if rect.collidepoint(event.pos):
                    select_sound.play()
                    brush.size = [20, 15, 10, 5][i]

            for color, rect in colors:
                if rect.collidepoint(event.pos):
                    brush.color = color

            # SAVE button
            if save_button.collidepoint(event.pos):
                select_sound.play()
                save_painting(brush.painting)

            # CLEAR button
            if clear_button.collidepoint(event.pos):
                select_sound.play()
                brush.clear()

    pygame.display.flip()

pygame.quit()
