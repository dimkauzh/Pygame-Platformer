# Modules
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

# Positions
mouse_pos = pygame.mouse.get_pos()
snail_x_pos = 600
snail_y_pos = 300
player_x_pos = 80
player_y_pos = 300

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
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

# Surfaces
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/Ground.png").convert()
text_surface = font.render("My game", False, "Black")

# Player + Bots (Moving Surfaces) + Converted images
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()

# Rectangles
player_rect = player_surface.get_rect(midbottom = (player_x_pos, player_y_pos))
snail_rect = snail_surface.get_rect(bottomright = (snail_x_pos, snail_y_pos))

# While loop while the game is running
while True:
    
    # Functions from before
    kill()
    blits()
    
    # Moving the snail
    snail_rect.x -= 3
    
    # Changes the direction that the snail goes
    if snail_rect.right <= 0:
        snail_rect.left = 800
    
    # Making player move
    player_rect.left += 1
    
    # CollideRect
    #if player_rect.colliderect(snail_rect):
    #    print("Collision")
    
    #Collidepoint mouse
    if player_rect.collidepoint(mouse_pos):
        print("Collision")
    
    # Update display
    pygame.display.update()
    clock.tick(60)