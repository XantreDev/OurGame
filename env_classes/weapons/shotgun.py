from env_classes.weapons.weapon import Weapon
from env_classes.weapons.auto_shotgun import AutoShotgun
from object_classes.bullet import bullet
from tools.utils import degree_editor

class Shotgun(AutoShotgun):
    def __init__(self, speeding = 20, scatter = 30, scatter_frequency = 1, Worker=None, Character=None):
        super().__init__(speeding=speeding, scatter=scatter, scatter_frequency=scatter_frequency, Worker=Worker, Character=Character)
    
    def run(self):
        super().run()
        self.deactivate()