import pygame
import os
import random
#necesario para inicializar la fuente que usaré para el marcador de puntos
pygame.init()

#propiedades de la ventana
WIN_WIDTH = 500
WIN_HEIGHT = 700

#importar,escalar y rotar imágenes
BIRD_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png")))  
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
PIPE_IMGDOWN = pygame.transform.flip(PIPE_IMG,False,True)

class Pipe:
    
    IMG = PIPE_IMGDOWN
    IMGDOWN = PIPE_IMG
    #espacio entre pipe y pipedown
    GAP = 250
    
    def __init__(self):
        self.x=WIN_WIDTH
        #determinar el alto de manera aleatoria
        self.height=random.randint(50,450)
        self.y=self.height-self.IMG.get_height()
        self.vel = 4
        # máscaras de ambas imagenes de las tuberias
        self.mask_up = pygame.mask.from_surface(self.IMG)
        self.mask_down = pygame.mask.from_surface(self.IMGDOWN)
        #comprueba si la tubería ha pasado al pajaro o no (se inicia a True por conveniencia)
        self.comprobar = True
        
    def detectarColision(self, bird):
        # calcular distancias entre pájaro y tuberías
        distancia_up = (self.x - bird.x, self.y - bird.y)
        distancia_down = (self.x - bird.x, self.height + self.GAP - bird.y)
        # comprobar si existe overlap entre la máscara y la posición del pájaro
        if bird.mask.overlap(self.mask_down,distancia_down) or bird.mask.overlap(self.mask_up,distancia_up):
            return True
        return False
        
    
    def draw(self,window):
        window.blit(self.IMGDOWN,(self.x,self.height+self.GAP))
        window.blit(self.IMG,(self.x,self.y))
        
        
    def move(self,ticks):
        # control de la dificultad según el tiempo transcurridos
        d = self.vel+ticks/200
        if d > 10:
            d=10
        self.x-=d

class Contador:
    #posicion del contador
    X = WIN_WIDTH - 80
    Y = 40
    def __init__(self):
        self.puntuacion=0
        #selección de tipo y tamaño de fuente
        self.font = pygame.font.SysFont('chalkduster.ttf', 72)
        #renderizado del texto 
        self.img = self.font.render(str(self.puntuacion), True, (0,0,0))
    def draw(self,window):
        window.blit(self.img, (self.X, self.Y))
    def comprobar(self,pipe,bird):
        #si la tubería no ha pasado al pájaro, se comprueba si lo ha pasado ya
        if pipe.comprobar:
            if pipe.x+pipe.IMG.get_width() < bird.x:
                #en caso de que si, se aumenta la puntuación y la propiedad comprobar de la pipe pasa a falso 
                #(pipe.comprobar se iniciará de nuevo a true según aparezca la siguiente y se inicie el constructor)
                self.puntuacion+=1
                self.img = self.font.render(str(self.puntuacion), True, (0,0,0))
                pipe.comprobar = False
            

class Bird:
    
    IMG = BIRD_IMG
    
    ANCHURA = 50
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.tilt = 0     
        self.tick_count = 0
        self.vel = 0
        self.mask = pygame.mask.from_surface(self.IMG)
        
    def draw(self,window):
        rotated_img = pygame.transform.rotate(self.IMG,self.tilt)
        new_rectangle = rotated_img.get_rect(center=self.IMG.get_rect(topleft = (self.x,self.y)).center)
        window.blit(rotated_img, new_rectangle.topleft)
        
    def jump(self): 
        self.tick_count=0
        self.vel=-12
        
    def move(self):
        self.tick_count += 1
        #detecta la colisión con el techo y hace que el pajaro rebote
        if self.y <= 0:
            d = 30
            self.tick_count+=7
        #detecta la colision con el suelo y modifica la posición del pajaro para que no caiga
        elif self.y+self.IMG.get_height() >= WIN_HEIGHT:
            d=0
            self.y = WIN_HEIGHT-self.IMG.get_height()-1
        else: 
            gravity=4
            d = self.vel * (self.tick_count/2) + 0.5*gravity*((self.tick_count/2))**2
            if d > 16:
                d=16
        self.y+=d
        
        
       
   
def draw_window(window,bird,pipe,contador):
    window.blit(BG_IMG,(0,0))
    bird.draw(window)
    pipe.draw(window)
    contador.draw(window)
    pygame.display.update()
     

def game():
    ticks=0
    bird=Bird(200,300)
    pipe=Pipe()
    contador = Contador()
    window=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    
    clock=pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        ticks+=1
        for event in pygame.event.get():
            # Detectar todos los eventos que se producen
            
            # Cuando se cierra el juego
            if event.type == pygame.QUIT:
                run=False
                
            # Cuadno el pajaro salta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

                       
        pipe.move(ticks)
        bird.move()
        contador.comprobar(pipe,bird)
        #se pierde cuando colisionamos con una pipe
        if pipe.detectarColision(bird):
            run = False
        #crea una nueva pipe cuando esta salga de la ventana
        if pipe.x + pipe.IMG.get_width() < 0:
            pipe=Pipe()
        draw_window(window,bird,pipe,contador)
    pygame.quit()
    quit()
    
game()