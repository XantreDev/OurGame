import pygame
import sys
from character.player import character
from screen import screen

def main():
    pygame.init()
    work=True
    S = screen()
    P = character()
    while work==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: work = False
            else: P.control_logic(event)
        P.process_logic()
        S.drawing(P)
    sys.exit()