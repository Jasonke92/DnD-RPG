from os import walk
import pygame
from wall import *



walkRight = [pygame.image.load('sprites/WalkR1.png'), pygame.image.load('sprites/WalkR2.png'), pygame.image.load('sprites/WalkR3.png'),pygame.image.load('sprites/WalkR4.png'), pygame.image.load('sprites/WalkR5.png'),pygame.image.load('sprites/WalkR6.png'),pygame.image.load('sprites/WalkR7.png'),pygame.image.load('sprites/WalkR8.png'),pygame.image.load('sprites/WalkR9.png'),pygame.image.load('sprites/WalkR10.png')]
walkLeft = [pygame.image.load('sprites/WalkL1.png'), pygame.image.load('sprites/WalkL2.png'), pygame.image.load('sprites/WalkL3.png'),pygame.image.load('sprites/WalkL4.png'), pygame.image.load('sprites/WalkL5.png'),pygame.image.load('sprites/WalkL6.png'),pygame.image.load('sprites/WalkL7.png'),pygame.image.load('sprites/WalkL8.png'),pygame.image.load('sprites/WalkL9.png'),pygame.image.load('sprites/WalkL10.png')]
walkUp = [pygame.image.load('sprites/WalkU1.png'), pygame.image.load('sprites/WalkU2.png'), pygame.image.load('sprites/WalkU3.png'),pygame.image.load('sprites/WalkU4.png'), pygame.image.load('sprites/WalkU5.png'),pygame.image.load('sprites/WalkU6.png'),pygame.image.load('sprites/WalkU7.png'),pygame.image.load('sprites/WalkU8.png'),pygame.image.load('sprites/WalkU9.png'),pygame.image.load('sprites/WalkU10.png')]
walkDown = [pygame.image.load('sprites/WalkD1.png'), pygame.image.load('sprites/WalkD2.png'), pygame.image.load('sprites/WalkD3.png'),pygame.image.load('sprites/WalkD4.png'), pygame.image.load('sprites/WalkD5.png'),pygame.image.load('sprites/WalkD6.png'),pygame.image.load('sprites/WalkD7.png'),pygame.image.load('sprites/WalkD8.png'),pygame.image.load('sprites/WalkD9.png'),pygame.image.load('sprites/WalkD10.png')]
idleDown = [pygame.image.load('sprites/IdleD1.png'), pygame.image.load('sprites/IdleD2.png'), pygame.image.load('sprites/IdleD3.png')]
idleRight = [pygame.image.load('sprites/IdleR1.png'), pygame.image.load('sprites/IdleR3.png')]
idleLeft = [pygame.image.load('sprites/IdleL1.png'), pygame.image.load('sprites/IdleL2.png'), pygame.image.load('sprites/IdleL3.png')]
idleUp = [pygame.image.load('sprites/IdleU1.png')]

walking = [walkRight, walkLeft, walkUp, walkDown, idleDown, idleRight, idleLeft, idleUp]
directions = ["Right", "Left", "Up", "Down", "IdleDown", "IdleRight", "IdleLeft", "IdleUp"]
rates = [6, 6, 6, 6, 20, 30, 20, 60]


class Player:
    
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.direction = "Down"
        self.lastpressed = "Down"
        self.vel = 5
        self.idle = 2
    
        
    def animate(self, display):

        for i in range(len(walking)):
            if self.direction ==  directions[i]:
                self.animation(walking[i], display, rates[i])
        self.walkCount +=1

    def animation(self, walk, display, rate):
        display.blit(walk[self.walkCount%60//rate], (self.x,self.y))
        self.walkCount = self.walkCount%60
        
        
    def move(self, player, objects, display):
        
        keys = pygame.key.get_pressed()

        if self.checkLeft(keys):
            self.idle = 0
            self.direction = "Left"
            self.lastpressed = self.direction
            if self.checkLeftHit(objects):
                self.x -= self.vel
        
        if self.checkRight(keys, display):
            self.idle = 0
            player.direction = "Right"
            player.lastpressed = player.direction
            if  self.checkRightHit(objects):
                player.x += self.vel
        
        if self.checkUp(keys):
            self.idle = 0
            player.direction = "Up"
            player.lastpressed = player.direction
            if  self.checkUpHit(objects):
                player.y -= self.vel

        if self.checkDown(keys, display):
            self.idle = 0
            player.direction = "Down"
            player.lastpressed = player.direction
            if self.checkDownHit(objects):
                player.y += self.vel
        else:
            if self.idle > 1:
                player.direction = "Idle" + player.lastpressed
            else:
                self.idle += 1


    def checkLeft(self, keys):
        if keys[pygame.K_a] and self.x > self.vel:
            return True

    def checkRight(self, keys, display):
        if keys[pygame.K_d] and self.x < display.width - self.width - self.vel:
            return True

    def checkUp(self, keys):
        if keys[pygame.K_w] and self.y > self.vel:
            return True

    def checkDown(self, keys, display):
        if keys[pygame.K_s] and self.y < (display.height - self.height - self.vel): 
            return True
            
    def checkLeftHit(self, objects):
        i = 1
        for object in objects:      
            if  self.x > (object.x + object.width +self.vel) or self.y > (object.y + object.height) or (self.y + self.height) < (object.y) or (self.x + self.width) < (object.x + self.vel):
                pass
            else:
                i = 0
        if i == 1:
            return True
            

    def checkRightHit(self, objects):
        i = 1 
        for object in objects: 
            if  self.x < object.x - self.width - self.vel or self.y > object.y + object.height or self.y + self.height < (object.y) or self.x > object.x + object.width - self.vel:
                pass
            else:
                i = 0
        if i == 1:
            return True

    def checkUpHit(self, objects):
        i = 1
        for object in objects: 
            if self.y > (object.y + object.height + self.vel) or self.x > (object.x + object.width) or (self.x + self.width) < (object.x) or self.y + self.height < object.y + self.vel: 
                pass
            else:
                i = 0 
        if i == 1:
            return True

    def checkDownHit(self, objects):
        i = 1
        for object in objects: 
            if self.y + self.height < object.y - self.vel or self.x > (object.x + object.width) or (self.x + self.width) < (object.x) or self.y > object.y + object.height - self.vel: 
                pass
            else:
                i = 0
        if i == 1:
            return True