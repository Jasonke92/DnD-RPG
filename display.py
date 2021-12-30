import pygame
# import sys

class Display: 

    def __init__(self, width, height, bg):
        self.width = width
        self.height = height
        self.bg = bg
        self.disp = pygame.display.set_mode((self.width, self.height))
        

    def create(self):
        background = pygame.image.load(self.bg)
        self.disp.blit(background,(0,0))

    def update(self):
        pygame.display.update()
