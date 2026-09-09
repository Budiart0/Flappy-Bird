import pygame
pygame.init()

width, height = 1280, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

background_img = pygame.image.load('bglong.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_img, (0, 0))
    pygame.display.update()