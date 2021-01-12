import pygame
import operations as ops
from constants import *

pygame.init()

COLOR_MAP = {
    "and": (43, 124, 164),
    "not": (146, 32, 25),
    "nand": (93, 36, 180),
    "or": (141, 78, 163),
    "xor": (187, 58, 119),
    "nor": (54, 116, 59),
    "xnor": (129, 160, 200)
}


class Operator:
    width, height = 200, 100
    font = pygame.font.SysFont("comicsans", 45)

    def __init__(self, x, y, name):
        self.x, self.y = x, y
        self.name = name.upper()
        self.func = getattr(ops, "_" + name.lower())
        self.color = COLOR_MAP[self.name.lower()]
        if self.name.lower() == "not":
            self.inputs = [Input(self, 1.5)]
            self.height = 60
        else:
            self.inputs = [Input(self, 1), Input(self, 2)]
        # self.output = Output()

    def update(self, win, events):
        mx, my = pygame.mouse.get_pos()
        self.draw(win)
        for input in self.inputs:
            input.update(win)
        # self.output.status = self.func(*self.inputs)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
                    return True
            if event.type == pygame.MOUSEBUTTONUP:
                return False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.name, 1, WHITE)
        win.blit(text, (self.x + self.width // 2 - text.get_width() // 2, self.y + self.height // 2 - text.get_height() // 3))

    def __repr__(self):
        return self.name


class Input:
    radius = 15
    color = (0, 0, 0)

    def __init__(self, host, index):
        self.host = host
        self.index = int((index - 1) * 2 + 1)
        self.x = self.y = 0
        self.output = None
        self.status = None

    def calc_pos(self):
        self.x = self.host.x
        self.y = int((self.host.height * (self.index / 4)) + self.host.y)

    def update(self, win):
        self.calc_pos()
        if self.output is not None:
            self.status = self.output.status
        self.draw(win)

    def mouse_release(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                return (x - self.x)**2 + (y - self.y)**2 <= self.radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def plug(self, output):
        self.output = output


class Path:
    width = 5

    def __init__(self, input, output):
        self.input, self.output = input, output
        input.plug(output)


class Text:
    height = 65
    y = 815
    font = pygame.font.SysFont("comicsans", 45)

    def __init__(self, x, text):
        self.x = x
        self.text = self.font.render(text.upper(), 1, WHITE)
        self.width = self.text.get_width() + 30
        self.color = (47, 47, 47)

    def update(self, win, events):
        self.draw(win)

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

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        win.blit(self.text, (self.x + self.width//2 - self.text.get_width()//2, self.y + self.height//2 - self.text.get_height()//3))
