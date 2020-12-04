import math, random, sys, pygame
from pygame.locals import *
# exit program
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
# definitions
black = 0,0,0
white = 255,255,255
size = width, height = 600, 600
HW,HH = width/2, height/2
# initialize game
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
FPS = 10               
### unit class ###
class Unit:
    def __init__(self,filename,x,y):
        self.sheet = pygame.image.load(filename)
        # minotaur spreadsheet coordinates
        self.frame = 0
        self.action = 0
        self.x = x
        self.y = y
        self.direction = "Left"
        #rect = x * y
        area = self.frame * self.action
    #increment self frame
    def update(self):
        self.frame = (self.frame + 1) % 10
        pass
    def draw(self,surface):
        xs = self.frame * 48 
        ys = self.action * 48  
        #pygame.mixer()
        cUnit = self.sheet
        isFlipped = pygame.transform.flip(cUnit, True, False)
        if self.direction == "Right":
            cUnit = isFlipped
        surface.blit (cUnit, (self.x,self.y), area=(xs, ys, 48, 48))          
m = Unit('minotaur.png',250,250) 
# minotaur behavior
STAND = 0
GROWL = 1
WALK = 2
ATTACK = 3
ALIVE = 4
# game loop
while 1:
    events() 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        m.action = WALK
        m.x-= 1
        m.direction = "Left"
    elif keys[pygame.K_RIGHT]:
        m.action = WALK
        m.x+= 1
        m.direction = "Right"
    elif keys[pygame.K_UP]:
        m.action = WALK
        m.y-= 1
    elif  keys[pygame.K_DOWN]:
        m.action = WALK
        m.y+= 1
    elif  keys[pygame.K_SPACE]:
        m.action = ATTACK
        #deal damage to opponent
    else:
        m.action = STAND  
    m.update()
    m.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(black)
        
       
       
       
       

