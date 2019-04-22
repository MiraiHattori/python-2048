#!/usr/bin/env python3

from build.game import init_game
from build.game import init_board
from build.game import print_result
from build.game import get_board
from build.game import exec_once
from build.game import get_score
from build.game import get_turn

from ai import AI
from tweet import tweet

if __name__ == '__main__':
    init_game()
    scores = 0
    turns = 0
    interval = 100
    ai = AI()
    i = -1
    try:
        while True:
            i += 1
            ai.initialize()
            init_board()
            if i % interval == interval - 1:
                debug_str = "{} games average; score: {} turn: {}".format(interval, scores / interval, turns / interval)
                tweet(debug_str)
                scores = 0
                turns = 0
            while True:
                exec_once(ai.move())
                # up, left, down, right
                if all([elem == 0 for elem in get_board()]):
                    scores += get_score()
                    turns += get_turn()
                    ai.finalize()
                    break
    except Exception as e:
        tweet("Exception from 2048 run.py: {}".format(e))
