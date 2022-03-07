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
import operations as ops
from constants import *

pygame.init()


class Operator:
    width = 200
    font = pygame.font.SysFont("comicsans", 45)

    def __init__(self, x, y, name, moving=False):
        self.x, self.y = x, y
        self.name = name.upper()
        self.func = getattr(ops, "_" + name.lower())
        self.color = COLOR_MAP[name.lower()]
        self.text_surf = self.font.render(self.name, 1, WHITE)
        self.moving = moving
        if name.lower() == "not":
            self.inputs = [Input(self, 1.5)]
            self.height = 60
        else:
            self.inputs = [Input(self, 1), Input(self, 2)]
            self.height = 100
        self.output = Output(self)

    def update(self, window):
        if self.moving:
            self.x, self.y = pygame.mouse.get_pos()
            self.x -= self.width/2
            self.y -= self.height/2
        self.draw(window)
        for input in self.inputs:
            input.draw(window)
        self.output.draw(window)
        if [inp.status for inp in self.inputs].count(None) == 0:
            self.output.status = self.func(*self.inputs)

    def hovered(self):
        mx, my = pygame.mouse.get_pos() 
        return self.x < mx < self.x + self.width and self.y < my < self.y + self.height

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        x = self.x + self.width / 2 - self.text_surf.get_width() / 2
        y = self.y + self.height / 2 - self.text_surf.get_height() / 3
        window.blit(self.text_surf, (x, y))

    def stop_moving(self):
        self.moving = False

    def start_moving(self):
        self.moving = True

    def in_bound(self):
        in_x = BOX[0] < self.x and self.x+self.width < BOX[0]+BOX[2]
        in_y = BOX[1] < self.y and self.y+self.height < BOX[1]+BOX[3]
        return in_x and in_y

    def __repr__(self):
        return self.name


class Input:
    radius = 15
    COLOR_HOVER = (170, 168, 170)
    COLOR_REST = (0, 0, 0)

    def __init__(self, host, index):
        self.host = host
        self.index = (index - 1) * 2 + 1
        self.x = self.y = 0
        self.output = None
        self.status = None

    def calc_pos(self):
        self.x = self.host.x
        self.y = (self.host.height * (self.index / 4)) + self.host.y
    
    def hovered(self):
        mx, my = pygame.mouse.get_pos()
        return (mx - self.x)**2 + (my - self.y)**2 <= self.radius**2

    def draw(self, window):
        self.calc_pos()
        if self.hovered():
            color = self.COLOR_HOVER
        else:
            color = self.COLOR_REST
        pygame.draw.circle(window, color, (self.x, self.y), self.radius)

    def plug(self, output):
        self.output = output


class Output:
    radius = 15
    COLOR_HOVER = (170, 168, 170)
    COLOR_REST = (0, 0, 0)

    def __init__(self, host):
        self.host = host
        self.x = self.y = 0
        self.status = None
        self.color = (0, 0, 0)

    def calc_pos(self):
        self.x = self.host.x + self.host.width
        self.y = self.host.y + self.host.height/2

    def hovered(self):
        mx, my = pygame.mouse.get_pos()
        return (mx - self.x)**2 + (my - self.y)**2 <= self.radius**2

    def draw(self, window):
        self.calc_pos()
        if self.hovered():
            color = self.COLOR_HOVER
        else:
            color = self.COLOR_REST
        pygame.draw.circle(window, color, (self.x, self.y), self.radius)


class Path:
    width = 5

    def __init__(self, output):
        self.output = output
        self.input = None
    
    def register(self, input):
        input.plug(self.output)
        self.input = input

    def draw(self, window):
        p1 = (self.output.x, self.output.y)
        p2 = pygame.mouse.get_pos()
        if self.input is not None:
            p2 = (self.input.x, self.input.y)
        
        color = (226, 22, 62) if self.output.status else (37, 35, 40)
        pygame.draw.line(window, color, p1, p2, self.width)
