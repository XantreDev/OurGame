import pygame
import math


pygame.init()
color = (73,24,19)

class character(pygame.sprite.Sprite):
    def __init__(self, hp = 100, ammo=100, x=600, y=800, size=40, speed = 10, img= 'Bob.png'):
        pygame.sprite.Sprite.__init__(self)
        self.hp=hp
        self.ammo=ammo
        self.image = pygame.image.load('character/Bob.png')
        self.image = pygame.transform.scale(self.image,(60,50))
        self.image = pygame.transform.rotate(self.image, 270)
        self.image_rotated = list()
        self.rect = self.image.get_rect()
        self.rect.center = (800,600)
        self.shift_x = 0
        self.shift_y = 0
        self.peeling_x = 0
        self.peeling_y = 0
        self.speed = speed
        self.a=0
        self.all_rotates()
        self.collide_x = False
        self.collide_y = False
        self.mouse_pos = (0,0)

    def all_rotates(self):
        x = pygame.image.load('character/Bob.png')
        x = pygame.transform.scale(x,(60,50))
        for i in range (0,721):
            self.image_rotated.append(pygame.transform.rotate(x, i/2))

    def control_logic(self, event):
        if event.type == pygame.KEYDOWN:
            if chr(event.key) == 'a':
                self.shift_x = -self.speed
            elif chr(event.key) == 'd':
                self.shift_x = self.speed
            if chr(event.key) == 'w':
                self.shift_y = -self.speed
            elif chr(event.key) == 's':
                self.shift_y = self.speed
        elif event.type == pygame.KEYUP:
            if chr(event.key) == 'a':
                self.shift_x = 0
            elif chr(event.key) == 'd':
                self.shift_x = 0
            if chr(event.key) == 'w':
                self.shift_y = 0
            elif chr(event.key) == 's':
                self.shift_y = 0
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos=event.pos

            # angle=(math.degrees(math.atan2(y1-y,x1-x)+math.pi))
            # print(angle)
            # if (round(angle*2) != round(self.a*2)):
            #      self.image = self.image_rotated[(180-round(angle))*2]
            #      self.a = angle

    def collide_with_lvl(self,lvl):
        self.collide_x = False
        self.collide_y = False
        for item in lvl.objects:
            if (item.collidepoint(self.rect.midtop) or item.collidepoint(self.rect.midbottom) or item.collidepoint(self.rect.topleft) or
            item.collidepoint(self.rect.bottomleft) or item.collidepoint(self.rect.topright) or item.collidepoint(self.rect.bottomright)):
                self.collide_y = True
            if (item.collidepoint(self.rect.midleft) or item.collidepoint(self.rect.midright) or item.collidepoint(self.rect.bottomleft)
                    or item.collidepoint(self.rect.topright) or item.collidepoint(self.rect.bottomright) or item.collidepoint(self.rect.topleft)):
                self.collide_x = True

    def collide(self, lvl):
        self.collide_with_lvl(lvl)

    def process_logic(self, lvl):
        x,y = self.rect.centerx, self.rect.centery
        self.rect.centerx +=self.shift_x
        self.rect.centery += self.shift_y
        self.collide(lvl)
        if (self.collide_x):
            self.rect.centerx = x
        if (self.collide_y):
            self.rect.centery = y
        self.rotation()

    def rotation(self):
        angle = (math.degrees(math.atan2(self.rect.centery - self.mouse_pos[1], self.rect.centerx - self.mouse_pos[0]) + math.pi))
        print(angle)
        if (round(angle * 2) != round(self.a * 2)):
            self.image = self.image_rotated[(180 - round(angle)) * 2]
            self.a = angle




    def draw(self, screen):
        screen.blit(self.image,self.rect)