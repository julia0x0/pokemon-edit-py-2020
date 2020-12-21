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
    increase = size[1]/480
    white = (255, 255, 255)
    black = (0, 0, 0)
    shapes = {}
    shape = None
    shape_type = "circle"
    shape_color = black
    pressed = False
    font = pygame.font.SysFont("Dejavu Sans Mono", int(25*increase))
    background = white
    buttons = {}
    button = None
    texts = {
        ("DRAW", ((0, 0, 0), (255, 255, 255))): "global tmp_type\ntmp_type='draw'", 
        ("EDIT", ((0, 0, 0), (255, 255, 255))): "global tmp_type\ntmp_type='edit'", 
        ("ATTR", ((0, 0, 0), (255, 255, 255))): "global tmp_type\ntmp_type='attr'"
    }
    desc_texts = {
        ("THET", ((0, 0, 0), (255, 255, 255))): "global tmp_type\ntmp_type='draw'", 
        ("THAT", ((0, 0, 0), (255, 255, 255))): "global tmp_type\ntmp_type='edit'", 
        ("THIT", ((0, 0, 0), (255, 255, 255))): "global tmp_type\ntmp_type='attr'"
    }
    move_type = "draw"
    index = -1
    FPS = 60
    clock = pygame.time.Clock()
    while True:
        screen.fill(background)
        if move_type == "draw":
            shapes, shape, pressed, move_type, index = check_draw(shapes, shape, shape_type, shape_color, pressed, buttons, move_type, index)
        elif move_type == "edit":
            move_type, index = check_edit(buttons, move_type, index)
        elif move_type == "attr":
            move_type, index = check_attr(buttons, move_type, index)
        load_drawings(screen, shapes, shape, shape_type, shape_color, size)
        buttons = load_all_buttons(screen, font, texts, desc_texts, increase, buttons, index, size)
        clock.tick(FPS)
        pygame.display.update()

def check_draw(shapes, shape, shape_type, shape_color, pressed, buttons, move_type, index):
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_type, i = check_pressed_buttons(buttons, position, move_type)
            if i < 0:
                shape = [position, (0, 0)]
                pressed = True
            else:
                index = i
        elif event.type == pygame.MOUSEBUTTONUP:
            if shape:
                shapes[tuple(shape)] = (shape_type, shape_color)
                shape = None
            pressed = False
        elif pressed:
            if shape:
                shape[1] = (abs(position[0] - shape[0][0]), abs(position[1] - shape[0][1]))
            else:
                shape = [position, position]
    return shapes, shape, pressed, move_type, index

def check_edit(buttons, move_type, index):
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_type, i = check_pressed_buttons(buttons, position, move_type)
            if i >= 0:
                index = i
    return move_type, index

def check_attr(buttons, move_type, index):
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_type, i = check_pressed_buttons(buttons, position, move_type)
            if i >= 0:
                index = i
    return move_type, index

def check_pressed_buttons(buttons, position, move_type):
    i = 0
    for startpos, endpos in buttons:
        width_bool = position[0] >= startpos[0] and position[0] <= endpos[0]
        height_bool = position[1] >= startpos[1] and position[1] <= endpos[1]
        if width_bool and height_bool:
            command = buttons.get((startpos, endpos))
            exec(command)
            pressed = True
            global tmp_type
            if tmp_type:
                move_type = tmp_type
                return move_type, i
        i += 1
    return move_type, -1

def load_all_buttons(screen, font, texts, desc_texts, increase, buttons, index, screen_size):
    buttons = load_buttons(screen, font, texts, increase, buttons, index, 0, screen_size, True)
    buttons = load_buttons(screen, font, desc_texts, increase, buttons, index, len(texts), screen_size, False)
    return buttons

def load_buttons(screen, font, texts, increase, buttons, index, start_i, screen_size, left: bool):
    add = 20*increase + font.size(" ")[1]
    if left:
        temp_position = [20*increase, 20*increase]
    else:
        temp_position = [screen_size[0] - (20*increase), 20*increase]
    length = 2
    i = start_i
    for text, colors in texts:
        if index == i:
            background, color = colors
        else:
            color, background = colors
        command = texts.get((text, colors))
        text_size = font.size(text)
        size = (text_size[0] + text_size[1]/3, text_size[1] + text_size[1]/3)
        if left:
            position = temp_position
        else:
            position = (temp_position[0] - text_size[0], temp_position[1])
        button = load_button(screen, font, text, command, color, background, position, size, text_size)
        buttons.update(button)
        temp_position[1] += add
        i += 1
    return buttons

def load_button(screen, font, text, command, color, background, position, size, text_size):
    rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, background, rect)
    position = (int(position[0]), int(position[1]))
    text_pos = (position[0] + (size[0] - text_size[0])/2, position[1] + (size[1] - text_size[1])/2)
    screen.blit(font.render(text, True, color), text_pos)
    end_pos = (int(abs(position[0] + size[0])), int(abs(position[1] + size[1])))
    return {(position, end_pos): command}

def load_drawings(screen, shapes, shape, shape_type, shape_color, size):
    if shape and len(shape) == 2:
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
