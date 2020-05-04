from object_classes.bullet import Bullet
from tools.utils import degree_editor


class Weapon:
    """
    Weapon chasis
    """
    def __init__(self, speeding=20, Worker=None, Character=None):
        self.worker = Worker
        self.character = Character
        self.speeding = speeding
        self.status = False
        self.timer = 0

    def activate(self):
        """
        Weapon acitvation
        """
        self.status = True

    def run(self):
        """
        Process of weapon
        """
        pass

    def deactivate(self):
        """
        Weapon deactivation
        """
        self.status = False


class AutoShotgun(Weapon):
    """
    Automatic shotgun class
    """
    def __init__(self, speeding=2, scatter=20, scatter_frequency=1, Worker=None, Character=None, speed=20):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)
        self.scatter_frequency = scatter_frequency
        self.scatter = scatter
        self.speed = speed

    def activate(self):
        """
        Weapon acitvation
        """
        super().activate()
        self.timer = 0

    def run(self):
        """
        Process of weapon
        """
        if self.status and self.timer % self.speeding == 0:
            for i in range(-self.scatter, self.scatter, self.scatter_frequency):
                angle = degree_editor(self.character.a + i)
                self.worker.add_object(Bullet(
                    (self.character.rect.centerx, self.character.rect.centery), angle, speed=self.speed))
            self.worker.add_object(Bullet(
                (self.character.rect.centerx, self.character.rect.centery), self.character.a, speed=self.speed))
        self.timer += 1


class Shotgun(AutoShotgun):
    def __init__(self, speeding=20, scatter=30, scatter_frequency=1, Worker=None, Character=None):
        super().__init__(speeding=speeding, scatter=scatter,
                         scatter_frequency=scatter_frequency, Worker=Worker, Character=Character)

    def run(self):
        """
        Weapon acitvation
        """
        super().run()
        self.deactivate()


class SemiautomaticGun(Weapon):
    def __init__(self, speeding=20, Worker=None, Character=None):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)

    def run(self):
        """
        Process of weapon
        """
        if self.status and self.timer % self.speeding == 0:
            self.worker.add_object(Bullet(
                (self.character.rect.centerx, self.character.rect.centery), self.character.a))
        self.deactivate()
        self.timer += 1


class AutomaticGun(Weapon):
    def __init__(self, speeding=1, scatter=3, Worker=None, Character=None):
        super().__init__(speeding=speeding, Worker=Worker, Character=Character)
        self.scatter = scatter
        self.scatter_formule = (self.scatter - 1) / 2

    def activate(self):
        """
        Weapon acitvation
        """
        super().activate()
        self.timer = 0

    def run(self):
        """
        Process of weapon
        """
        if self.status and self.timer % self.speeding == 0:
            angle = self.character.a
            angle += (self.timer % self.scatter) - self.scatter_formule
            angle = degree_editor(angle)
            self.worker.add_object(
                Bullet((self.character.rect.centerx, self.character.rect.centery), angle))
        self.timer += 1
