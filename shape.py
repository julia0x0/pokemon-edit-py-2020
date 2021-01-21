import pygame, os
from pygame import Surface, Color, Rect
from pygame.font import SysFont, Font
from enum import Enum


class Shape(Enum):
    Rectangle = 1,
    Circle = 2

class Text(Surface):
    def __init__(self, text: str, position: tuple = (0, 0), color: Color = Color(255, 255, 255), antialias: bool = True,  font_info: tuple = ("Arial", 16)):
        self.font = SysFont(font_info[0], font_info[1])
        self.position = position
        self = self.font.render(text, antialias, color)


class Image(Surface):
    def __init__(self, filename: str, position: tuple = (0, 0), folder: str = os.path.join(os.getcwd(), "img")):
        self.position = position
        self.path = os.path.join(folder, filename)
        self = pygame.image.load(self.path)


class Rectangle(Surface):
    def __init__(self, size: tuple, position: tuple = (0, 0), text: Text = None, background: Color = Color(0, 0, 0), image: Image = None, width: int = 0, border_radius: int = 0):
        super().__init__(size)
        self.position = position
        self.size = size
        self.background = background
        self.width = width
        self.border_radius = border_radius
        self.image = image
        self.text = text
        self.update()

    def resize(self, x: int, y: int):
        self.size = (x-self.position[0], y+self.position[1])
        self.update()

    def move(self, x: int, y: int):
        self.position = (x, y)
        self.update()

    def update(self):
        super().__init__(self.size)
        self.rect = Rect((0, 0), self.size)
        pygame.draw.rect(self, self.background, self.rect, self.width, self.border_radius)
        if self.image:
            self.draw(self.image)
        if self.text:
            self.draw(self.text)

    def draw(self, surface):
        self.blit(surface, surface.position)


class Circle(Rectangle):
    def __init__(self, size: tuple = (5, 5), position: tuple = (0, 0), text: Text = None, background: Color = Color(0, 0, 0), image: Image = None, width: int = 0):
        super().__init__(size, position, text, background, image, width, min(height, width) / 2)


class Container(Rectangle):
    def __init__(self, size: tuple = (5, 5), position: tuple = (0, 0), text: Text = None, background: Color = Color(0, 0, 0), image: Image = None, width: int = 0, border_radius: int = 0, shapes: list = []):
        self.shapes = shapes
        super().__init__(size, position, text, background, image, width, border_radius)

    def append(self, shape: Shape):
        super().append(shape)
        self.update()

    def remove(self, shape: Shape):
        super().remove(shape)
        self.update()

    def update(self):
        super().update()
        for shape in self.shapes:
            self.draw(shape)
