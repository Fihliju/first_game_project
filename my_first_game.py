import pygame
import random
def drawplayer():

 pygame.init()
 clock= pygame.time.Clock()

 global width, height
 width=800
 height=500
 Background=(135,206,235)
 screen=pygame.display.set_mode((width,height))

while True:
 screen.fill((Background))
 drawplayer()
 clock.tick(30)
 pygame.display.update()
