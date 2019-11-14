import pygame


pygame.init()
color = (73,24,19)

class character:
    def __init__(self, hp = 100, ammo=100, x=600, y=800, size=40, speed = 10):
        self.hp=hp
        self.ammo=ammo
        self.rect = pygame.Rect(x,y,size,size//2)
        self.shift_x = 0
        self.shift_y = 0
        self.speed = speed
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



    def process_logic(self):
        self.rect.centerx +=self.shift_x
        self.rect.centery += self.shift_y

    def draw(self, screen):
        pygame.draw.rect(screen,color,self.rect)