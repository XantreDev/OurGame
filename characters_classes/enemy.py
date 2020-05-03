from os.path import normpath, normcase
from env_classes.weapons import AutoShotgun, AutomaticGun
from characters_classes.character import character
from tools.path_finder import pathfinder
import math as math

class Enemy(character):
    def __init__(self, img = normpath('resources/images/character/Bob.png'), coordinates=(0, 0), weapon=AutomaticGun, Worker=None):
        super().__init__(img=img, weapon=weapon, Worker=Worker)
        self.rect.center = coordinates
    
    def run(self, player, precision = 80):
        path = pathfinder((self.rect.centerx // precision, self.rect.centery // precision),
                          (player.rect.centerx // precision, player.rect.centery // precision))
        print(path)
        if len(path)>1:
            x, y = path[1]
        else: x, y = path[0]
        self.rect.center = (x*precision, y*precision)

        self.rotate_to_player(player)
    
    def rotate_to_player(self, player):
        angle = self.angle(player)
        if (round(angle * 2) != round(self.a * 2)):
            self.image = self.image_rotated[(180 - round(angle)) * 2]
            self.a = angle
    
    
    def angle(self, player):
        angle = 180 - ((math.pi * math.atan2(self.rect.centery - player.rect.centery, 
                                      self.rect.centerx - player.rect.centerx)) 
                 / 180)
        return angle