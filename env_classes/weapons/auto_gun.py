from env_classes.weapons.weapon import Weapon
from object_classes.bullet import bullet
from random import randint

class AutomaticGun(Weapon):
    def __init__(self, speeding = 1, scatter = 10, Worker=None, Character=None):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)
        self.scatter = scatter
        self.scatter_formule = (self.scatter - 1) / 2
    
    def activate(self):
        super().activate()
        self.timer = 0
    
    def run(self):
        if self.status and self.timer % self.speeding == 0:
            angle = self.character.a
            angle += self.timer % self.scatter - self.scatter_formule
            if angle < 0:
                angle = 360 - angle
            elif angle > 360:
                angle = angle - 360
            self.worker.object_adder(bullet((self.character.rect.centerx, self.character.rect.centery), angle))
        self.timer += 1
