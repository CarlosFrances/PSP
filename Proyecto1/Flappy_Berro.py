import pygame
import os
import random

WIN_WIDTH = 500
WIN_HEIGHT = 700
GAP = 200

BERRO_IMG=pygame.image.load(os.path.join("imgs","berro.jpg"))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))
       
        
    
    

class Berro:
    
    IMG = BERRO_IMG
    
    ANCHURA = 50
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        
        self.tick_count = 0
        self.vel = 0
        self.img=self.IMG
        
    def draw(self,window):
        rotated_img = pygame.transform.rotate(self.img,self.tilt)
        new_rectangle = rotated_img.get_rect(center=self.img.get_rect(topleft = (self.x,self.y)).center)
        window.blit(rotated_img, new_rectangle.topleft)
        
    def jump(self): 
        self.tick_count=0
        self.tilt+=90
        self.vel=-12
        
    def move(self):
        self.tick_count += 1
        
        gravity=3
        d = self.vel * self.tick_count + 0.5*gravity*(self.tick_count)**2
        if d > 16:
            d=16
        
        self.y+=d
        
       
   
def draw_window(window,berro):
    window.blit(BG_IMG,(0,0))
    berro.draw(window)
    pygame.display.update()
     


def game():
    berro=Berro(200,300)
    window=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    
    clock=pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            #Detectar todos los eventos que se producen
            
            #Cuando se cierra el juego
            if event.type == pygame.QUIT:
                run=False
                
            #Cuadno el pajaro salta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    berro.jump()

        berro.move()
        draw_window(window,berro)
    pygame.quit()
    quit()
    
game()