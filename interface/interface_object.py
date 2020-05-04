import pygame
from characters_classes.deafult_object import GameObject


class InterfaceObject(GameObject):
    def __init__(self, character):
        size = (60, 6)
        self.char = character
        
        x, y = self.char.rect.topleft
        y -= 15
        super().__init__(pygame.Rect((x, y), size))
        
        self.color = (0, 255, 0)

    def update(self):
        self.move(
            (self.char.rect.midtop[0] - self.rect.midtop[0]),
            (self.char.rect.midtop[1] - self.rect.midtop[1])
        )

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
