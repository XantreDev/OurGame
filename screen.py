import pygame

pygame.init()
width = 1600
height = 900
black = (0,0,0)
size = (width,height)

class screen(pygame.sprite.Sprite):
    def __init__(self, size= (1600,900), black =(0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.image.load("levels/background/background1.png")
        self.size=size
        self.black = black

    def drawing(self, character, level):
        self.screen.fill(self.black)
        self.screen.blit(self.background, self.background.get_rect())
        level.draw(self.screen)
        #self.screen.blit(self.image,self.image.get_rect())
        character.draw(self.screen)

    def return_screen(self):
        return self.screen