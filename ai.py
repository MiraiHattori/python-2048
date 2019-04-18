from build.game import is_movable_up_left_down_right
from build.game import get_board

def move():
    movable = is_movable_up_left_down_right()
    board = get_board()
    if movable[0]:
        return "up"
    elif movable[1]:
        return "left"
    elif movable[2]:
        return "down"
    elif movable[3]:
        return "right"
    else:
        return "quit"
