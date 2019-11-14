import pygame

pygame.init()
width = 1600
height = 900
black = (0,0,0)
size = (width,height)

class screen:
    def __init__(self, size= (1600,900), black =(0,0,0)):
        self.screen = pygame.display.set_mode(size)
        self.image = pygame.image.load("levels/map1.png")
        self.rect = self.image.get_rect()
        self.size=size
        self.black = black
    def drawing(self, character):
        self.screen.fill(self.black)
        self.screen.blit(self.image,self.rect)
        character.draw(self.screen)
        pygame.display.flip()
        pygame.time.wait(12)