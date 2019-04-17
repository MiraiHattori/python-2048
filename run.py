#!/usr/bin/env python3

from build.game import init_game
from build.game import init_board
from build.game import print_result
from build.game import get_board

from ai import move

if __name__ == '__main__':
    init_game()
    for i in range(100):
        init_board()
        while True:
            move()
            # up, left, down, right
            if all([elem == 0 for elem in get_board()]):
                break
    print_result()
