from os.path import normpath, normcase
from env_classes.weapons import AutoShotgun, AutomaticGun, SemiautomaticGun
from characters_classes.character import character
from tools.path_finder import Graph, pathfinder
import math as math
import settings
from tools.route import Route
from tools.utils import Vector, comprasion, more_accurate_comprasion


class Enemy(character):
    def __init__(self, img=normpath('resources/images/character/Bob.png'), cord=(200, 400), player=None, weapon=SemiautomaticGun, Worker=None):
        super().__init__(img=img, weapon=weapon, Worker=Worker)
        self.rect.center = cord
        self.player = player
        self.timer = 0
        self.path = []
        self.destination_point = None
        self.moving = False

    def run(self, objects):
        if not Route(self.rect.center, self.player.rect.center).roadblocks(objects):
            self.moving = False
            self.shift_x = 0
            self.shift_y = 0
            self.weapon.activate()
        else:
            x, y = self.player.rect.center
            x //= settings.precision
            y //= settings.precision
            if ( not self.path or (comprasion(self.player.block, (self.path[-1][1], self.path[-1][0])))):
                                #    and (self.destination_point not in Graph().neighbors((y, x))and self.destination_point != (y, x)))):
                path = pathfinder((self.rect.y // settings.precision, self.rect.x // settings.precision),
                                  (self.player.rect.y // settings.precision, self.player.rect.x // settings.precision))
                print(path)
                self.path = path
                self.destination_point = path[-1]
                print(self.player.block, (self.path[-1][1], self.path[-1][0]))
        if self.path:
            self.go_on_path()
        self.rotate_to_player(self.player)
        self.process_logic()
        self.weapon.run()
        self.hp_indicator.update()

    def process_logic(self, *args):
        self.move(self.shift_x, self.shift_y)

    def go_on_path(self):
        x, y = self.rect.centerx, self.rect.centery
        
        passed = -1
        
        
        for i in range(len(self.path)):
            if more_accurate_comprasion((y, x), (self.path[i][0] * settings.precision, self.path[i][1]*settings.precision)):
                passed = i + 1
        
        
        if passed != -1 or self.moving==False:
            # print("before: " ,self.path)
            self.moving = True
            self.path = self.path[passed:]
        
            if not self.path: return
                   
            # print("after: " ,self.path)
            
            target_y, target_x = self.path[0][0] * settings.precision, self.path[0][1] * settings.precision

            x//= settings.precision
            x*= settings.precision
            
            y//= settings.precision
            y*= settings.precision

            vector = Vector((target_x - x), (target_y - y))
            
            # print(vector.x, vector.y)
            
            k = 0.02
            
            self.shift_x = vector.x * k
            self.shift_y = vector.y * k
                
        
        
        
        # СТАРАЯ РЕАЛИЗАЦИЯ 
        # if not self.path:
        #     return
        
        # x_on_matrix = x // settings.precision
        # y_on_matrix = y // settings.precision
        # passed = 0

        # for i in range(len(self.path)):
        #     if (y_on_matrix, x_on_matrix) == self.path[i]:
        #         passed = i + 1

        # i = 0

        # # if (x_on_matrix == self.path[0][1] and y_on_matrix == self.path[0][0]):
        # #     del self.path[0]

        # self.path = self.path[passed:]

        # # while i < len(self.path) and passed > 0:
        # #     if i <= passed:
        # #         del self.path[i]
        # #         passed -= 1
        # #     else:
        # #         i += 1
        
        # if not self.path:
        #     return

        # # print(self.path)

        # into_y, into_x = (self.path[0][0] * settings.precision,
        #                   self.path[0][1] * settings.precision)
        # vector = Vector((into_x - x), (into_y - y))
        # if vector.x + vector.y == 0:
        #     k = 0
        # else:
        #     k = self.speed ** 2 / (vector.x ** 2 + vector.y ** 2)
        # k *= 2
        # self.shift_x = vector.x * k
        # self.shift_y = vector.y * k

    def rotate_to_player(self, player):
        angle = self.angle(player)
        if (round(angle * 2) != round(self.a * 2)):
            self.image = self.image_rotated[(180 - round(angle)) * 2]
            self.a = angle

    def angle(self, player):
        return (math.degrees(math.atan2(self.rect.centery - player.rect.centery,
                                        self.rect.centerx - player.rect.centerx)
                             + math.pi))
