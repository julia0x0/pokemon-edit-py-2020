def check_click(selected, ctrl, selection):
    if selected and ctrl:
        if selection in selected:
             selected.remove(selection)
        else:
            selected.append(selection)
    else:
        selected = [selection]
    return selected

def check_click_in_shape(shapes, position):
    selected = None
    for startpos, size in shapes.keys():
        endpos = (startpos[0]+size[0], startpos[1]+size[1])
        width_bool = position[0] >= startpos[0] and position[0] <= endpos[0]
        height_bool = position[1] >= startpos[1] and position[1] <= endpos[1]
        if width_bool and height_bool:
            selected = (startpos, size)
    return selected

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
