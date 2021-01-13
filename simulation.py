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
        self.output = Output(self)

    def update(self, window, events):
        mx, my = pygame.mouse.get_pos()
        self.draw(window)
        for input in self.inputs:
            input.update(window)
        self.output.update(window)
        if all([inp.status for inp in self.inputs]):
            self.output.status = self.func(*self.inputs)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
                    return True
            if event.type == pygame.MOUSEBUTTONUP:
                return False

    def hovered(self):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pygame.mouse.get_pos())
    
    def hovered_inps(self):
        for inp in self.inputs:
            if inp.hovered():
                return inp
        
        return False
    
    def hovered_out(self):
        return self.output.hovered()

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.name, 1, WHITE)
        window.blit(text, (self.x + self.width // 2 - text.get_width() // 2, self.y + self.height // 2 - text.get_height() // 3))

    def __repr__(self):
        return self.name


class Input:
    radius = 15

    def __init__(self, host, index):
        self.host = host
        self.index = int((index - 1) * 2 + 1)
        self.x = self.y = 0
        self.output = None
        self.status = None
        self.color = (0, 0, 0)

    def calc_pos(self):
        self.x = self.host.x
        self.y = int((self.host.height * (self.index / 4)) + self.host.y)

    def update(self, window):
        self.calc_pos()
        self.draw(window)
        if self.output is not None:
            self.status = self.output.status
        if self.hovered():
            self.color = (170, 168, 170)
        else:
            self.color = (0, 0, 0)

    def mouse_release(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                return self.hovered()
    
    def hovered(self):
        return ((pygame.mouse.get_pos()[0] - self.x)**2 + (pygame.mouse.get_pos()[1] - self.y)**2)**0.5 <= self.radius

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def plug(self, output):
        self.output = output


class Output:
    radius = 15

    def __init__(self, host):
        self.host = host
        self.x = self.y = 0
        self.status = None
        self.color = (0, 0, 0)

    def calc_pos(self):
        self.x = self.host.x + self.host.width
        self.y = self.host.y + self.host.height/2

    def update(self, window):
        self.calc_pos()
        self.draw(window)
        if self.hovered():
            self.color = (170, 168, 170)
        else:
            self.color = (0, 0, 0)

    def mouse_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.hovered()

    def hovered(self):
        return ((pygame.mouse.get_pos()[0] - self.x)**2 + (pygame.mouse.get_pos()[1] - self.y)**2)**0.5 <= self.radius

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


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


class OperatorManager:
    def __init__(self):
        self.x, self.y, self.width, self.height = BOX
        self.ops = []
        self.paths = []
        self.moving_op = None
    
    def update(self, window, events):
        for op in self.ops:
            op.update(window, events)
        
