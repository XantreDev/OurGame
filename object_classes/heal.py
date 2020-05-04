import settings
from object_classes.temp_object import TemporaryObject

class HealObject(TemporaryObject):
    def __init__(self, cord, Worker = None):
        size = settings.heal_size
        color = (0, 255, 0)
        super().__init__(cord, size, color, Worker = Worker)
        self.player = self.worker.characters[0]
    
    def run(self, *args):
        super().run(*args)
        if self.player.rect.colliderect(self.rect) and not self.off_frame:
            self.player.heal()
            self.off_frame = True
    
    def draw(self, screen):
        if not self.off_frame:
            super().draw(screen)
        
    