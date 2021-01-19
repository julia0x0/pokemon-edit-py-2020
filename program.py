import pygame, os
from shape import *
from modes import *
from enum import Enum


class Program(Container):
    def __init__(self, screen_size: Size = Size(1920, 1080), path: str = os.path.join("..", "saves", "untitled"), caption: str = "Create a Pokemon Game"):
        super().__init__(self, screen_size)
        self.path = path
        self.caption = caption
        self.

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.caption)
        self.screen.blit(self, self.position)

    def save(self):
        pass

    def stop(self):
        self.save()
        pygame.exit()
        sys.exit()
