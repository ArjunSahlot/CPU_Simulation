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
from interface import Text

pygame.init()


class Board:
    POSSIBLE_OPERATIONS = ["not", "and", "nand", "or", "xor", "nor", "xnor"]

    def __init__(self):
        self.x, self.y, self.width, self.height = BOX
        self.texts = []
        self.ops = []
        self.paths = []
        self.moving_op = None

        self.setup()

    def setup(self):
        prev = BOX[0]

        for op in self.POSSIBLE_OPERATIONS:
            t = Text(prev, op)
            self.texts.append(t)
            prev += t.width+1
    
    def update(self, window, events):
        for op in self.ops:
            op.update(window, events)
        for text in self.texts:
            text.draw(window)
