#
#  Cpu simulation
#  A simulation created in pygame in which you can explore how logic gates work.
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import pygame
import os
from constants import *
from simulation import *
from interface import *

pygame.init()

# Window Management
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CPU Simulation")


def draw_window(window):
    window.fill((47, 47, 47))
    pygame.draw.rect(window, (43, 43, 43), BOX, border_radius=10)
    pygame.draw.rect(window, (60, 60, 60), BOX, 10, border_radius=10)


def main(window, width, height):
    clock = pygame.time.Clock()
    paths = []
    ops = []
    texts = {
        "not": Text(50, "not"),
        "and": Text(144, "and"),
        "nand": Text(243, "nand"),
        "or": Text(364, "or"),
        "xor": Text(440, "xor"),
        "nor": Text(536, "nor"),
        "xnor": Text(634, "xnor"),
    }

    while True:
        clock.tick(FPS) 
        draw_window(window)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
