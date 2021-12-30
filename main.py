import pygame
import sys
from player import *
from wall import *
from display import Display
import numpy


#Display Variables
background = 'backgrounds/Background.jpg'
width = 1147
height = 646
display = Display(width, height, background)

#Wall Variables
wall1 = Wall(0, 0, 70, 360)
wall2 = Wall(0, 0, 575, 50)
wall3 = Wall(690, 0, 450, 150)
wall4 = Wall(1075, 0, 100, 600)
wall5 = Wall(0, 510, 1200, 100)



walls = []
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)
walls.append(wall5)


#Door Variables
door1 = Door(575, 0, 100, 60)

doors = []
doors.append(door1)


colObjects = numpy.concatenate((walls, doors))


for x in colObjects:
    print()



#Player Variables
pwidth = 92
pheight = 100
player = Player(500, 300, pwidth, pheight)

#Other Variables
clock = pygame.time.Clock()


while True: 
    #Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    
    #Loads Objects
    display.create()

    for x in doors:
        x.visible(display.disp)
    
    # for x in walls:
    #     x.visible(display.disp)

    #Controls Player
    player.move(player, colObjects, display)
    player.animate(display.disp)
    door1.unlock()
    # door1.lock()

    #Refresher
    clock.tick(60)
    display.update()