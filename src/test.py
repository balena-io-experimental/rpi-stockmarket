
import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
# Uncomment if you have a touch panel and find the X value for your device
#os.environ["SDL_MOUSEDRV"] = "TSLIB"
#os.environ["SDL_MOUSEDEV"] = "/dev/input/eventX"

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((240, 320), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((16, 0), (111, 106), (36, 277), (56, 27), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (40, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (110, 200, 40, 80), 1)
box = pygame.draw.rect(DISPLAYSURF, RED, (100, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[120][144] = BLACK
pixObj[122][146] = BLACK
pixObj[124][148] = BLACK
pixObj[126][158] = BLACK
pixObj[126][158] = BLACK
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Pos: %sx%s\n" % pygame.mouse.get_pos())
            if box.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
    pygame.display.update()
