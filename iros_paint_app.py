import pygame

pygame.init()
pygame.mixer.init()

import pygame.gfxdraw  # For drawing anti-aliased shapes


import os
from datetime import datetime



select_sound = pygame.mixer.Sound('select_sound.ogg')

fps = 120
timer = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

active_size = 0
active_color = "white"

screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption("Iro's paint app ")
painting = []



def draw_rounded_rect(surface, color, rect, radius):
	####"""Draw a rounded rectangle using pygame.gfxdraw"""
	x, y, w, h = rect
	# Draw the rounded corners
	pygame.gfxdraw.aacircle(surface, x + radius, y + radius, radius, color)
	pygame.gfxdraw.aacircle(surface, x + w - radius - 1, y + radius, radius, color)
	pygame.gfxdraw.aacircle(surface, x + radius, y + h - radius - 1, radius, color)
	pygame.gfxdraw.aacircle(surface, x + w - radius - 1, y + h - radius - 1, radius, color)
	
	# Fill the rounded rectangle
	pygame.gfxdraw.filled_circle(surface, x + radius, y + radius, radius, color)
	pygame.gfxdraw.filled_circle(surface, x + w - radius - 1, y + radius, radius, color)
	pygame.gfxdraw.filled_circle(surface, x + radius, y + h - radius - 1, radius, color)
	pygame.gfxdraw.filled_circle(surface, x + w - radius - 1, y + h - radius - 1, radius, color)
	
	# Fill the rectangular parts
	pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
	pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))






##### Main game loop done.
##### first, set brush sizes.
def draw_menu(size, color):
	pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 70])
	pygame.draw.line(screen, "black", (0, 70), (WIDTH, 70), 3)


	xl_brush = pygame.draw.rect(screen, "black", [10, 10, 50, 50])
	pygame.draw.circle(screen, "white", (35, 35), 20)

	l_brush = pygame.draw.rect(screen, "black", [70, 10, 50, 50])
	pygame.draw.circle(screen, "white", (95, 35), 15)

	m_brush = pygame.draw.rect(screen, "black", [130, 10, 50, 50])
	pygame.draw.circle(screen, "white", (155, 35), 10)

	s_brush = pygame.draw.rect(screen, "black", [190, 10, 50, 50])
	pygame.draw.circle(screen, "white", (215, 35), 5)
### brush list
	brush_list=[xl_brush, l_brush, m_brush, s_brush]


### borders
	if size == 20:
		pygame.draw.rect(screen, "green", [10, 10, 50, 50], 3)
	elif size == 15:
		pygame.draw.rect(screen, "green", [70, 10, 50, 50], 3)
	elif size == 10:
		pygame.draw.rect(screen, "green", [130, 10, 50, 50], 3)
	elif size == 5:
		pygame.draw.rect(screen, "green", [190, 10, 50, 50], 3)




	pygame.draw.circle(screen, color, (400, 35), 30)
	pygame.draw.circle(screen, color, (400, 35), 30, 3)

### colors:
	blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
	red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
	green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
	yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])


	teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
	purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
	white = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
	black = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])



# Save button (left of clear button)
	save_button_rect = [WIDTH - 290, 10, 80, 50]
	draw_rounded_rect(screen, (255, 255, 255), save_button_rect, 10)
	save_button = pygame.draw.rect(screen, (100, 255, 100), save_button_rect, border_radius=10)
	font = pygame.font.SysFont('Arial', 20)
	save_text = font.render('SAVE', True, (0, 0, 0))
	screen.blit(save_text, (WIDTH - 277, 25))





# Clear button with rounded rectangle background
	clear_button_rect = [WIDTH - 200, 10, 80, 50]
	
	# Draw white rounded rectangle background first
	draw_rounded_rect(screen, (255, 255, 255), clear_button_rect, 10)
	
	# Then draw the red button on top
	clear_button = pygame.draw.rect(screen, (255, 100, 100), clear_button_rect, border_radius=10)


	# Clear button (right corner)
	## clear_button = pygame.draw.rect(screen, (255, 100, 100), [WIDTH - 205, 10, 80, 50])
	font = pygame.font.SysFont('Arial', 20)
	clear_text = font.render('CLEAR', True, (0, 0, 0))
	screen.blit(clear_text, (WIDTH - 194, 25))

	color_rect = [blue, red, green, yellow, teal, purple, white, black]
	rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), 
				(0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]


	return brush_list, color_rect, rgb_list, clear_button, save_button
	######## !!!!
def draw_painting(paints):
	for i in range(len(paints)):
		pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

def save_painting():
	##"""Save painting with multiple fallback locations and detailed error reporting"""
		save_locations = [
			os.path.join(os.getenv('LOCALAPPDATA'), 'pygame_saves'),  # First try: AppData
			os.path.join(os.path.expanduser('~'), 'Desktop', 'pygame_saves'),  # Second try: Desktop
			os.path.join(os.path.expanduser('~'), 'Documents', 'pygame_saves'),  # Third try: Documents
			'pygame_saves'  # Final fallback: Current directory
		]
		for save_dir in save_locations:
			try:
				# Create directory if needed
				os.makedirs(save_dir, exist_ok=True)
			
				# Test write permission
				test_file = os.path.join(save_dir, 'permission_test.tmp')
				with open(test_file, 'w') as f:
					f.write("test")
				os.remove(test_file)

				# Create save surface
				save_surface = pygame.Surface((WIDTH, HEIGHT - 70))
				save_surface.fill((255, 255, 255))
				for color, pos, size in painting:
					pygame.draw.circle(save_surface, color, (pos[0], pos[1] - 70), size)

				# Generate filename
				timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
				filename = os.path.join(save_dir, f"painting_{timestamp}.png")

				# Save the file
				pygame.image.save(save_surface, filename)
			
				# Show success message
				font = pygame.font.SysFont('Arial', 24)
				msg = font.render(f"Saved to {filename}", True, (0, 200, 0))
				screen.blit(msg, (WIDTH//2 - 150, HEIGHT - 40))
				pygame.display.flip()
				pygame.time.delay(2000)  # Show for 2 seconds
			
				print(f"Successfully saved to: {filename}")
				return True

			except PermissionError:
				print(f"No write permission in {save_dir}, trying next location...")
				continue
			except Exception as e:
				print(f"Error saving to {save_dir}: {str(e)}")
				continue

		# If all locations failed
		print("Failed to save painting - no writable locations found")
		font = pygame.font.SysFont('Arial', 24)
		msg = font.render("Save failed - no writable locations", True, (200, 0, 0))
		screen.blit(msg, (WIDTH//2 - 150, HEIGHT - 40))
		pygame.display.flip()
		pygame.time.delay(2000)
		return False

	






###
run = True
while run:
	timer.tick(fps)
	screen.fill("white")
	mouse = pygame.mouse.get_pos()

	########## code with problem ?
	left_click = pygame.mouse.get_pressed()[0]
	##########

	
	######### remove if theres a bug
	if left_click and mouse[1] > 70:
		painting.append((active_color, mouse, active_size))
	draw_painting(painting)
	#########
	if mouse[1] > 70:
		pygame.draw.circle(screen, active_color, mouse, active_size)
	brushes, colors, rgbs, clear_button, save_button = draw_menu(active_size, active_color)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(len(brushes)):
				if brushes[i].collidepoint(event.pos):
					select_sound.play()
					active_size = 20 - (i * 5) ### figure this formula on your own if you wanna add more brushes!!
				

			for i in range(len(colors)):
					if colors[i].collidepoint(event.pos):
						active_color = rgbs[i] ### figure this formula on your own if you wanna add more brushes!!


			# Check clear button
			if clear_button.collidepoint(event.pos):
				select_sound.play()
				painting = []  # Clear all drawings

			# Check save button
			if save_button.collidepoint(event.pos):
				select_sound.play()
				save_painting()

					



	pygame.display.flip()
pygame.quit()



