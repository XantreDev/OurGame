import settings
import pygame
from object_classes.temp_object import TemporaryObject

class Blood(TemporaryObject):
    blood_color = (152, 0, 2)
    def __init__(self, cord, Worker = None):
        super().__init__(cord, settings.blood_size, color = self.blood_color, Worker=Worker)
        