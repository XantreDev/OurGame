import pygame
import sys
from character.player import character
from screen import screen
from lvl_init import lvl

def main():
    pygame.init()
    work=True
    S = screen()
    P = character()
    L = lvl()
    while work==True:
        #k = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: work = False
            else: P.control_logic(event)
            #k+=1
            #if (k>3): break
        P.process_logic()
        P.collide(L)
        S.drawing(P,L)
    sys.exit()