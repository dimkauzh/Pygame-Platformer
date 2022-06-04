import pygame
from sys import exit

h = 200
w = 100

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("2D Game")
clock = pygame.time.Clock()
def kill():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
def blits():
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/Ground.png")


while True:
    kill()
    blits()
    pygame.display.update()
    clock.tick(60)