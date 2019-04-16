#!/usr/bin/env python3

from build.game import init_game
from build.game import print_result
from build.game import exec_once
from build.game import is_movable_up_left_down_right

if __name__ == '__main__':
    for i in range(100):
        init_game()
        while True:
            # 1手
            movable = is_movable_up_left_down_right()
            if movable[0]:
                board = exec_once("up")
            elif movable[1]:
                board = exec_once("left")
            elif movable[2]:
                board = exec_once("down")
            elif movable[3]:
                board = exec_once("right")
            else:
                board = exec_once("quit")
            if all([elem == 0 for elem in board]):
                break
            #print(board)
    print_result()
