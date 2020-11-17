import pygame
import os
from CPU_Simulation.constants import *


# Window Management
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CPU_Simulation, By: ArjunSahlot")


def draw_window(win):
    win.fill(WHITE)


def main(win, width, height):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        draw_window(win)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                # exit()
        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
