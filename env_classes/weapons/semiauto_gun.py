from env_classes.weapons.weapon import Weapon
from object_classes.bullet import bullet

class SemiautomaticGun(Weapon):
    def __init__(self, speeding = 20, Worker=None, Character=None):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)
    
    def run(self):
        if self.status and self.timer % self.speeding == 0:
            self.worker.object_adder(bullet((self.character.rect.centerx, self.character.rect.centery), self.character.a))
        self.deactivate()
        self.timer += 1