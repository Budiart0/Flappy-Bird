import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

width, height = 1280, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

ground_scroll = 0
scroll_speed = 2

background_img = pygame.image.load('bglong.png')
ground_img = pygame.transform.scale(pygame.image.load('ground.png'),(1400, 168))

class Bird:
    def __init__(self, x, y):
        self.image = pygame.image.load('bird1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

bird = Bird(100, height // 2)

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
    bird.draw(screen)
    pygame.display.update()
    clock.tick(60)




