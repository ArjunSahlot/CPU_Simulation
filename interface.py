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
