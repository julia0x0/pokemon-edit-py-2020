#!/usr/bin/env python
import pygame, json, os
from pokemon_edit.modes import *
from pokemon_edit.load import *

def init():
    pygame.init()
    with open(os.path.join(os.getcwd(), "saves", "data.json"), 'r') as raw:
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
    blue = (0, 155, 255)
    shapes = {}
    shape = None
    shape_type = "rectangle"
    shape_color = black
    select_color = blue
    old_selected = []
    selected = []
    pressed = False
    ctrl = False
    fps_font = pygame.font.SysFont("Dejavu Sans Mono", int(10*increase))
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
        "draw": {
            ("COLOR", ((0, 0, 0), (255, 255, 255))): "global tmp_color\ntmp_color='get_color()'", #get_color func
            ("SHAPE", ((0, 0, 0), (255, 255, 255))): "global tmp_shape\ntmp_shape='rectangle'"
        },
        "edit": {
            ("COLOR", ((0, 0, 0), (255, 255, 255))): "global tmp_sub_type\ntmp_sub_type='get_color()'", #implement get_color func
            ("SIZE", ((0, 0, 0), (255, 255, 255))): "global tmp_size\ntmp_size='get_size()'", #implement get_size func 
            ("DELETE", ((0, 0, 0), (255, 255, 255))): "global tmp_sub_type\ntmp_sub_type='attr'"
        },
        "attr": {
            ("RAW", ((0, 0, 0), (255, 255, 255))): "global tmp_sub_type\ntmp_sub_type='raw'",
            ("TYPE", ((0, 0, 0), (255, 255, 255))): "global tmp_sub_type\ntmp_sub_type='type'",
            ("COMMAND", ((0, 0, 0), (255, 255, 255))): "global tmp_sub_type\ntmp_sub_type='command'"
        }
    }
    move_type = "edit"
    index = 1
    FPS = 60
    clock = pygame.time.Clock()
    while True:
        desc_text = desc_texts.get(move_type)
        screen.fill(background)
        if move_type == "draw":
            move_type, index, shapes, shape, pressed, selected = check_draw(shapes, shape, shape_type, shape_color, pressed, buttons, move_type, index)
        elif move_type == "edit":
            move_type, index, shapes, selected, ctrl = check_edit(buttons, shapes, move_type, index, selected, ctrl)
        elif move_type == "attr":
            move_type, index, selected = check_attr(buttons, shapes, move_type, index)
        load_drawings(screen, shapes, shape, shape_type, shape_color, size, selected, select_color)
        buttons = load_all_buttons(screen, font, texts, desc_text, increase, buttons, index, size)
        load_fps(screen, clock, fps_font)
        clock.tick()
        pygame.display.update()
