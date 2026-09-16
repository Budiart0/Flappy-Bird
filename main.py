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
        self.image = [pygame.image.load('bird1.png'), pygame.image.load('bird2.png'), pygame.image.load('bird3.png')]
        self.rect = self.image[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame_count = 0
            self.frame += 1
            if self.frame >= len(self.image):
                self.frame = 0

    def jump(self):
        keys = pygame.key.get_pressed()
        global wait_time
        if keys[pygame.K_SPACE] :
            self.rect.y -= 90
            wait_time = 10

    def gravity(self):
        self.rect.y += 1

    def draw(self, screen):
        screen.blit(self.image[self.frame], (self.rect.x, self.rect.y))

class Pipe:
    def __init__(self, x, y, height, is_top):
        self.image1 = pygame.transform.scale(pygame.image.load('pipe.png'), (80, height))
        self.rect1 = self.image1.get_rect()
        self.rect1.x = x
        self.rect1.y = y + 360

        self.image2 = pygame.transform.scale(pygame.transform.flip(self.image1, False, True), (80, height))
        self.rect2 = self.image2.get_rect()
        self.rect2.x = x
        self.rect2.y = y


    def draw(self, screen):
        screen.blit(self.image1, (self.rect1.x, self.rect1.y))
        screen.blit(self.image2, (self.rect2.x, self.rect2.y))

bird = Bird(100, height // 2)
pipe = Pipe(500, 0, 240, True)
wait_time = 0

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
    bird.update()
    bird.gravity()
    print(wait_time)
    if wait_time == 0:
        bird.jump()
    else:
        wait_time -= 1
    bird.draw(screen)
    pipe.draw(screen)
    pygame.display.update()
    clock.tick(60)




