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

    moving_ops = None
    text_clicking = False

    run = True
    while run:
        clock.tick(FPS)
        draw_window(window)
        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for name, text in texts.items():
            state = text.update(window, events)
            if state:
                moving_ops = Operator(text.x, text.y, name)
                ops.append(moving_ops)
                text_clicking = True
            elif state is not None and moving_ops is not None and text_clicking:
                if BOX[0] < moving_ops.x and moving_ops.x + moving_ops.width < BOX[0] + BOX[2] and BOX[1] < moving_ops.y and moving_ops.y + moving_ops.height < BOX[1] + BOX[3]:
                    ops.append(moving_ops)

                moving_ops = None
                text_clicking = False

        for op in ops:
            state = op.update(window, events)
            if state:
                ops.remove(op)
                moving_ops = op
                break
            elif state is not None and moving_ops is not None:
                if BOX[0] < moving_ops.x and moving_ops.x + moving_ops.width < BOX[0] + BOX[2] and BOX[1] < moving_ops.y and moving_ops.y + moving_ops.height < BOX[1] + BOX[3]:
                    ops.append(moving_ops)

                moving_ops = None

        if moving_ops is not None:
            moving_ops.update(window, events)
            moving_ops.x, moving_ops.y = mx - moving_ops.width // 2, my - moving_ops.height // 2

        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
