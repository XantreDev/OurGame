from env_classes.weapons.weapon import Weapon
from object_classes.bullet import bullet
from tools.utils import degree_editor

class AutoShotgun(Weapon):
    def __init__(self, speeding = 2, scatter = 20, scatter_frequency = 1, Worker=None, Character=None, speed = 20):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)
        self.scatter_frequency = scatter_frequency
        self.scatter = scatter
        self.speed = speed
    
    def activate(self):
        super().activate()
        self.timer = 0
    
    def run(self):
        if self.status and self.timer % self.speeding == 0:
            for i in range(-self.scatter, self.scatter, self.scatter_frequency):
                angle = degree_editor(self.character.a + i)
                self.worker.object_adder(bullet((self.character.rect.centerx, self.character.rect.centery), angle, speed=self.speed))
            self.worker.object_adder(bullet((self.character.rect.centerx, self.character.rect.centery), self.character.a, speed=self.speed))
        self.timer += 1