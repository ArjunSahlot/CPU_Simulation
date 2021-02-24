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
from constants import *
pygame.init()


class Text:
    height = 65
    y = 815
    font = pygame.font.SysFont("comicsans", 45)

    def __init__(self, x, text):
        self.x = x
        self.text = self.font.render(text.upper(), 1, WHITE)
        self.width = self.text.get_width() + 30
        self.color = (47, 47, 47)

    def update(self, window, events):
        self.draw(window)

        if pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pygame.mouse.get_pos()):
            self.color = (62, 62, 62)
        else:
            self.color = (47, 47, 47)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pygame.mouse.get_pos()):
                    return True
            if event.type == pygame.MOUSEBUTTONUP:
                if not pygame.Rect(50, self.y, 704, self.height).collidepoint(pygame.mouse.get_pos()):
                    return False

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        window.blit(self.text, (self.x + self.width//2 - self.text.get_width()//2, self.y + self.height//2 - self.text.get_height()//3))
