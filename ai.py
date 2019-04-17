from build.game import exec_once
from build.game import is_movable_up_left_down_right
from build.game import get_board

def move():
    movable = is_movable_up_left_down_right()
    board = get_board()
    if movable[0]:
        exec_once("up")
    elif movable[1]:
        exec_once("left")
    elif movable[2]:
        exec_once("down")
    elif movable[3]:
        exec_once("right")
    else:
        exec_once("quit")
