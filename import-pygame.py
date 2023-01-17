import pygame 
import pygame.locals

from random import randint
from math import sqrt

pygame.init() 

#Define Window Size 
width = 800 
height = 600

#Define Colors 
black = (0, 0, 0) 
white = (255, 255, 255) 

#Create Window
window = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('Cannon Blasters') 

#Create Background
background = pygame.Surface(window.get_size()) 
background.fill(black) 

#Game Objects 
class Cannon(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((20, 20)) 
        self.image.fill(white) 
        self.rect = self.image.get_rect() 
        self.rect.centerx = x 
        self.rect.centery = y

class Target(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((20, 20)) 
        self.image.fill(white) 
        self.rect = self.image.get_rect() 
        self.rect.centerx = x 
        self.rect.centery = y

#Create Sprites
cannon = Cannon(width/2, height-20) 
target = Target(randint(20, width-20), randint(20, height-20))

#Game Loop
running = True
while running: 
    #Handle Events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
            
    #Update 
    dist = sqrt((cannon.rect.centerx - target.rect.centerx)**2 + (cannon.rect.centery - target.rect.centery)**2)
    if dist < 20: 
        target.rect.centerx = randint(20, width-20) 
        target.rect.centery = randint(20, height-20) 
        
    #Draw 
    window.blit(background, (0, 0)) 
    window.blit(cannon.image, cannon.rect) 
    window.blit(target.image, target.rect) 
    pygame.display.flip() 

pygame.quit()