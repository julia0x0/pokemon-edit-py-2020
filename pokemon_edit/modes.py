import pygame, sys
from pokemon_edit.check import *

def check_draw(shapes, shape, shape_type, shape_color, pressed, buttons, move_type, index):
    selected = []
    position = pygame.mouse.get_pos()
    for event in [pygame.event.wait()]+pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_type, i = check_pressed_buttons(buttons, position, move_type)
            if i < 0:
                shape = [position, (0, 0)]
                pressed = True
            else:
                index = i
        elif event.type == pygame.MOUSEBUTTONUP:
            if shape:
                shapes[tuple(shape)] = [shape_type, shape_color]
                shape = None
            pressed = False
        elif pressed:
            if shape:
                shape[1] = (abs(position[0] - shape[0][0]), abs(position[1] - shape[0][1]))
            else:
                shape = [position, position]
    return move_type, index, shapes, shape, pressed, selected

def check_edit(buttons, shapes, move_type, index, selected, ctrl):
    position = pygame.mouse.get_pos()
    for event in [pygame.event.wait()]+pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                ctrl = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                ctrl = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_type, i = check_pressed_buttons(buttons, position, move_type)
            selection = check_click_in_shape(shapes, position)
            if i < 0:
                selected = check_click(selected, ctrl, selection)
            else:
                index = i
    return move_type, index, shapes, selected, ctrl

def check_attr(buttons, shapes, move_type, index):
    selected = []
    position = pygame.mouse.get_pos()
    for event in [pygame.event.wait()]+pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_type, i = check_pressed_buttons(buttons, position, move_type)
            selection = check_click_in_shape(shapes, position)
            if i < 0:
                selected = check_click(selected, ctrl, selection)
            else:
                index = i
    return move_type, index, selected