import pygame
import sys
from characters_classes.player import Player
from screen import screen
from env_classes.level import level


def main():
    pygame.init()
    work=True
    S = screen()
    P = Player()
    L = level()
    while work==True:
        events_array = list()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: work = False
            elif event.type == pygame.KEYDOWN and chr(event.key) == 'o':
                L.level_creator(S.return_screen())
            else: events_array.append(event)
        P.logic(L, events_array)
        S.drawing(P,L)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()