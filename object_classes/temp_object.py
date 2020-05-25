import pygame
from characters_classes.deafult_object import GameObject


class TemporaryObject(GameObject):
    def __init__(self, cord, size, color, Worker=None):
        super().__init__(pygame.Rect(cord, size))
        self.worker = Worker
        self.color = color
        self.active = True
        self.timer = 0

    def run(self, *args):
        self.timer += 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
