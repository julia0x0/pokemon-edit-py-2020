#!/usr/bin/env python
import pygame, json, sys, os

def init():
    pygame.init()
    with open(os.path.join("out", "data.json"), 'r') as raw:
        data = json.load(raw)
    size = data.get("size")
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Draw Scene or Menu for Pokemon")
    return screen, data, size

def main():
    screen, data, size = init()
    white = (255, 255, 255)
    black = (0, 0, 0)
    shapes = {}
    shape = None
    shape_type = "rectangle"
    shape_color = black
    pressed = False
    background = white
    FPS = 60
    clock = pygame.time.Clock()
    while True:
        screen.fill(background)
        shapes, shape, pressed = check_movement(shapes, shape, shape_type, shape_color, pressed)
        load_drawings(screen, shapes, shape, shape_type, shape_color, size)
        clock.tick(FPS)
        pygame.display.update()

def check_movement(shapes, shape, shape_type, shape_color, pressed):
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shape = [position, None]
            pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if shape:
                shapes[tuple(shape)] = (shape_type, shape_color)
                shape = None
            pressed = False
        elif pressed:
            if shape:
                shape[1] = (position[0] - shape[0][0], position[1] - shape[0][1])
            else:
                shape = [position, position]
    return shapes, shape, pressed

def load_drawings(screen, shapes, shape, shape_type, shape_color, size):
    if shape:
        if shape[0] and shape[1]:
            load_drawing(screen, shape[0], shape[1], shape_type, shape_color)
    for position, size in shapes:
        type, color = shapes.get((position, size))
        load_drawing(screen, position, size, type, color)

def load_drawing(surface, position, size, type, color):
    rect = pygame.Rect(position, size)
    if type == "rectangle":
        pygame.draw.rect(surface, color, rect)
    elif type == "circle":
        pygame.draw.ellipse(surface, color, rect)

def stop():
    sys.exit()

if __name__ == "__main__":
    main()
