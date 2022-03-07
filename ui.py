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

from typing import List, Optional
import pygame
from constants import *
from interface import Text
from simulation import Operator, Path

pygame.init()


class Board:
    POSSIBLE_OPERATIONS = ["not", "and", "nand", "or", "xor", "nor", "xnor"]

    def __init__(self):
        self.x, self.y, self.width, self.height = BOX
        self.texts: List[Text] = []
        self.ops: List[Operator] = []
        self.paths: List[Path] = []
        self.moving_op: Optional[Operator] = None
        self.moving_path: Optional[Path] = None

        self.setup()

    def setup(self):
        prev = BOX[0]

        for op in self.POSSIBLE_OPERATIONS:
            t = Text(prev, op)
            self.texts.append(t)
            prev += t.width + 1

    def update(self, window, events):
        mx, my = pygame.mouse.get_pos()
        mld = mrd = mlu = mru = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mld = event.button == 1
                mrd = event.button == 3
            if event.type == pygame.MOUSEBUTTONUP:
                mlu = event.button == 1
                mru = event.button == 3
        md = mld or mrd
        mu = mlu or mru

        # Handle current operators
        rem = None
        for op in self.ops:
            op.update(window)
        for i, op in enumerate(reversed(self.ops)):
            if mld and op.hovered():
                rem = len(self.ops) - i - 1
                self.moving_op = op
                self.moving_op.start_moving()
                break

        if rem is not None:
            self.ops.pop(rem)

        # Handle creating operators
        for text in self.texts:
            text.draw(window)

            if mld and text.hovered():
                self.moving_op = Operator(mx, my, text.name, True)

        # Handle active operator in motion
        if self.moving_op is not None:
            self.moving_op.update(window)
            if mu:
                self.moving_op.stop_moving()
                if self.moving_op.in_bound():
                    self.ops.append(self.moving_op)
                self.moving_op = None
