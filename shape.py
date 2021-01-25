import pygame, os
from pygame import Surface, Color, Rect
from pygame.font import Font, SysFont
from enum import Enum


class Shape(Enum):
    Rectangle = 1,
    Circle = 2

class Text(object):
    def __init__(self, text: str, font: Font, position: tuple = (0, 0), color: Color = Color(255, 255, 255), antialias: bool = True):
        self.font = font
        self.text = text
        self.color = color
        self.antialias = antialias
        self.position = position
        self.rendered = self.font.render(self.text, self.antialias, self.color)


class Image(Surface):
    def __init__(self, filename: str, position: tuple = (0, 0), folder: str = os.path.join(os.getcwd(), "img")):
        self.position = position
        self.path = os.path.join(folder, filename)
        self.image = pygame.image.load(self.path)


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
        self.size = (abs(x-self.position[0]), abs(y-self.position[1]))
        self.update()

    def move(self, x: int, y: int):
        self.position = (x, y)
        self.update()

    def update(self):
        super().__init__(self.size)
        self.rect = Rect((0, 0), self.size)
        print((self.background, self.rect, self.width, self.border_radius))
        pygame.draw.rect(self, self.background, self.rect, self.width, self.border_radius)
        if self.image:
            self.draw_image(self.image)
        if self.text:
            self.draw_text(self.text)

    def draw_image(self, image: Image):
        self.blit(image.image, image.position)

    def draw_text(self, text: Text):
        self.blit(text.rendered, text.position)

    def draw(self, surface):
        self.blit(surface, surface.position)


class Circle(Rectangle):
    def __init__(self, size: tuple = (5, 5), position: tuple = (0, 0), text: Text = None, background: Color = Color(0, 0, 0), image: Image = None, width: int = 0):
        super().__init__(size, position, text, background, image, width, min(size[0], size[1]) / 2)


class Container(Rectangle):
    def __init__(self, size: tuple = (5, 5), position: tuple = (0, 0), text: Text = None, background: Color = Color(255, 255, 255), image: Image = None, width: int = 0, border_radius: int = 0, shapes: list = []):
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
