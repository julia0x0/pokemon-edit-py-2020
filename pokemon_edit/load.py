import pygame

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

def load_drawings(screen, shapes, shape, shape_type, shape_color, size, selected, select_color):
    if shape and len(shape) == 2:
        if shape[0] and shape[1]:
            load_drawing(screen, shape[0], shape[1], shape_type, shape_color, [], select_color)
    for position, size in shapes.keys():
        value = shapes.get((position, size))
        type, color = value
        load_drawing(screen, position, size, type, color, selected, select_color)

def load_drawing(surface, position, size, type, color, selected, select_color):
    if (position, size) in selected:
        color = select_color
    rect = pygame.Rect(position, size)
    if type == "rectangle":
        pygame.draw.rect(surface, color, rect)
    elif type == "circle":
        pygame.draw.ellipse(surface, color, rect)

def load_fps(screen, clock, font, color=(0, 0, 0), aa=True):
    fps = str(int(clock.get_fps()))
    screen.blit(font.render(f"{fps} FPS", aa, color), (0, 0))
