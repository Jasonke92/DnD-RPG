import pygame

doorimg = pygame.image.load('objects/Door.png')

class Wall:


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def visible(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

class Door(Wall):



    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.open = False


    def visible(self, display):
        display.blit(doorimg, (self.x,self.y))

    def unlock(self):
        if not self.open:
            self.x = -1 * (self.x)
            self.open = True

    def lock(self):
        if self.open:
            self.x = -1 * (self.x)
            self.open = False

    
