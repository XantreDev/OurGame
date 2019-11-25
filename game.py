import pygame
import sys
from characters_classes.player import Player
from screen import screen
from lvl_init import lvl

def main():
    pygame.init()
    work=True
    S = screen()
    P = Player()
    L = lvl()
    while work==True:
        #k = 0
        events_array = list()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: work = False
            else: events_array.append(event)
        P.logic(L, events_array)
        S.drawing(P,L)
    sys.exit()