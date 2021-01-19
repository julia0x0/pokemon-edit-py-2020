import pygame, os
from pygame import Surface, Font, Color, Rect
from enum import Enum


class Shape(Enum):
    Rectangle = 1,
    Circle = 2


class Position(tuple):
    def __init__(self, x: int, y: int):
        super().__init__((x, y))

    def change(self, x: int, y: int):
        super().__init__((x, y))

class Size(Position):
    pass

class Text(Surface):
    def __init__(self, font: text: str, position: Position = Position(0, 0), color: Color = Color(255, 255, 255), antialias: bool = True):
        self.position = position
        self = font.render(text, antialias, color)


class Image(Surface):
    def __init__(self, filename: str, position: Position = Position(0, 0), folder: str = os.path.join(os.getcwd(), "img")):
        self.position = position
        self.path = os.path.join(folder, filename)
        self = pygame.image.load(self.path)


class Rectangle(Surface):
    def __init__(self, size: Size = Size(5, 5) position: Position = Position(0, 0), background: Color or Image = Color(255, 255, 255), width: int = 0, border_radius: int = 0):
        super().__init__(size)
        self.position = position
        self.size = size
        self.color = Color(255, 255, 255)
        if background is Color:
            self.color = background
        self.width = width
        self.border_radius = border_radius
        self.image = None
        if background is Image:
            self.image = background
        self.update()

    def resize(self, x: int, y: int):
        self.size.change(x, y)
        self.update()

    def move(self, x: int, y: int):
        self.position.change(x, y)
        self.update()

    def update(self):
        super().__init__(self.size)
        self.rect = Rect(Position(0, 0), self.size)
        pygame.draw.rect(self, self.color, self.rect, self.width, self.border_radius)
        if self.image:
            self.blit(self.image, self.image.position)


class Circle(Rectangle):
    def __init__(self, size: Size = Size(5, 5) position: Position = Position(0, 0), background: Color or Image = Color(255, 255, 255), width: int = 0):
        super().__init__(size, position, background, width, min(height, width) / 2)


class Container(Rectangle):
    def __init__(self, size: Size = Size(5, 5) position: Position = Position(0, 0), background: Color or Image = Color(255, 255, 255), width: int = 0, border_radius: int = 0, shapes: list = []):
        super().__init__(size, position, background, width, border_radius)
        self.shapes = shapes

    def append(self, shape: Shape):
        super().append(shape)
        self.update()

    def remove(self, shape: Shape):
        super().remove(shape)
        self.update()

    def update(self):
        super().update()
        for shape in self.shapes:
            self.blit(shape, shape.position)
