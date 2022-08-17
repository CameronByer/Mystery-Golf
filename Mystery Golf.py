import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mystery Golf")
clock = pygame.time.Clock() ## For syncing the FPS

class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = 0
        self.chargespot = None

    def getspeed(self): # Feet per second
        return (self.speedx**2+self.speedy**2)**0.5

    def setspeed(self, speed): # Feet per second
        curspeed = self.getspeed()
        if curspeed != 0:
            self.speedx *= speed/curspeed
            self.speedy *= speed/curspeed

    def draw(self, camera):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 5)

    def update(self):
        if self.getspeed() <= 5:
            self.setspeed(0)
        else:
            self.setspeed(self.getspeed()*(1-0.5/FPS))
        # (Feet/Sec)/(Frame/Sec) = Feet/Frame
        self.x += self.speedx/FPS
        self.y += self.speedy/FPS

    def launch(self, release):
        if self.chargespot != None and self.getspeed() == 0:
            chargex, chargey = self.chargespot
            releasex, releasey = release
            self.speedx = chargex - releasex
            self.speedy = chargey - releasey
            self.chargespot = None

b = Ball(100, 50)
b.speedx = 1

## Game loop
running = True
while running:

    clock.tick(FPS) ## will make the loop run at the same speed all the time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click
                b.chargespot = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                b.launch(pygame.mouse.get_pos())

    screen.fill(DARKGREEN)

    b.update()
    b.draw(None)

    pygame.display.flip()       

pygame.quit()
