import pygame
import sys
from player import *
pygame.init()

display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


player = Player(400, 300, 32, 32)

while True: 
    display.fill((24,164,86))

    #Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    keys = pygame.key.get_pressed()

    
        
    player.main(display)

    #Controls Player
    if keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_s]:
        player.y += 5

    clock.tick(60)
    pygame.display.update()