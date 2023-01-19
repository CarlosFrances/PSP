import pygame
import os
import random

WIN_WIDTH = 500
WIN_HEIGHT = 700

BIRD_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
PIPE_IMGDOWN = pygame.transform.flip(PIPE_IMG,False,True)


class Pipe:
    IMG_UP = PIPE_IMG
    IMG_DOWN = PIPE_IMGDOWN
    GAP = 200


    def __init__(self):
        self.x = WIN_HEIGHT
        self.height = random.randint(50,450)
        self.top = self.height-self.IMG_UP.get_height()


    def draw(self, window):
        window.blit(self.IMG_DOWN,(self.x,self.top))
        window.blit(self.IMG_UP,(self.x,self.height+self.GAP))
        
    def move(self):
        self.x-=5




class Bird:
    IMG = BIRD_IMG
    ANCHURA = 50

    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.tick_count = 0
        self.vel = 0
        self.img = self.IMG
        self.tilt = 0

    def jump(self):
        self.vel = -12
        self.tick_count = 0

    def draw(self,window):
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rectangle = rotated_img.get_rect(center=self.img.get_rect(topleft=(self.x,self.y)).center)
        window.blit(rotated_img, new_rectangle.topleft)

    def move(self):
        self.tick_count += 1

        gravity = 3
        d = self.vel*self.tick_count + 0.5*gravity*(self.tick_count)**2

        if d > 16:
            d = 16

        self.y += d


def draw_window(window, bird, pipe):
    window.blit(BG_IMG, (0, 0))
    bird.draw(window)
    pipe.draw(window)
    pygame.display.update()


def game():
    bird = Bird(200, 300)
    pipe = Pipe()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            # Detectar todos los eventos que se producen

            # Cuando se cierra el juego
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        bird.move()
        pipe.move()

        
        draw_window(window, bird,pipe)

    pygame.quit()
    quit()



game()