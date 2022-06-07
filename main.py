import pygame
from sys import exit

# Launch the game
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("2D Game")

# FPS
clock = pygame.time.Clock()

# Font
font = pygame.font.Font("font/Pixeltype.ttf", 50)

# For stopping game(Moving)Surfaces
def kill():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Surfaces + Moving Surfaces
def blits():
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, snail_y_pos))

# Surfaces
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/Ground.png")
text_surface = font.render("My game", False, "Black")

# Player + Bots (Moving Surfaces)
snail_surface = pygame.image.load("graphics/snail/snail1.png")

# Snail position
snail_x_pos = 600
snail_y_pos = 265

# Loop while game is running
while True:
    kill()
    blits()
    pygame.display.update()
    clock.tick(60)