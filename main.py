import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

width, height = 1280, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

ground_scroll = 0
scroll_speed = 4

background_img = pygame.image.load('bglong.png')
ground_img = pygame.image.load('ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_img, (0, 0))
    screen.blit(ground_img, (ground_scroll, 768 - ground_img.get_height()))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    pygame.display.update()
    clock.tick(60)




