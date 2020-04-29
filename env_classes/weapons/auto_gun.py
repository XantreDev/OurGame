from random import randint

from env_classes.weapons.weapon import Weapon
from object_classes.bullet import bullet
from tools.utils import degree_editor


class AutomaticGun(Weapon):
    def __init__(self, speeding = 1, scatter = 3, Worker=None, Character=None):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)
        self.scatter = scatter
        self.scatter_formule = (self.scatter - 1) / 2
    
    def activate(self):
        super().activate()
        self.timer = 0
    
    def run(self):
        if self.status and self.timer % self.speeding == 0:
            angle = self.character.a
            angle += (self.timer % self.scatter) - self.scatter_formule
            angle = degree_editor(angle)
            self.worker.object_adder(bullet((self.character.rect.centerx, self.character.rect.centery), angle))
        self.timer += 1
