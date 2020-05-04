from os.path import normpath, normcase
from env_classes.weapons import AutoShotgun, AutomaticGun, SemiautomaticGun
from characters_classes.character import character
from tools.path_finder import pathfinder
import math as math
import settings
from tools.route import Route


class Enemy(character):
    def __init__(self, img=normpath('resources/images/character/Bob.png'), coordinates=(0, 0), player = None, weapon=SemiautomaticGun, Worker=None):
        super().__init__(img=img, weapon=weapon, Worker=Worker)
        self.rect.center = coordinates
        self.player = player
        self.timer = 0

    def run(self, objects):
        if not Route(self.rect.center, self.player.rect.center).roadblocks(objects):
            self.weapon.activate()
        else:
            path = pathfinder((self.rect.centery // settings.precision, self.rect.centerx // settings.precision),
                              (self.player.rect.centery // settings.precision, self.player.rect.centerx // settings.precision))
            # print(path)
            if len(path) > 1:
                y, x = path[1]
            else:
                y, x = path[0]
            self.rect.center = (x*settings.precision, y*settings.precision)

        self.rotate_to_player(self.player)

        self.weapon.run()
        self.hp_indicator.update()

        self.timer+=1
        

    def rotate_to_player(self, player):
        angle = self.angle(player)
        if (round(angle * 2) != round(self.a * 2)):
            self.image = self.image_rotated[(180 - round(angle)) * 2]
            self.a = angle

    def angle(self, player):
        return (math.degrees(math.atan2(self.rect.centery - player.rect.centery,
                                        self.rect.centerx - player.rect.centerx)
                             + math.pi))

