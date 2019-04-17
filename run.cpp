#include <numeric>
#include <vector>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "game/game.hpp"

void initGame()
{
    using Game::game;
    game = std::make_unique<Game::Game>();
}

void initBoard()
{
    using Game::game;
    game->init();
}

void printResult()
{
    using Game::game;
    game->printResult();
}

std::array<int, COL_SIZE * ROW_SIZE> getBoard()
{
    using Board::board;
    return board->pybind11Board();
}

void execOnce(std::string command)
{
    using Game::game;
    game->execOnce(command);
}

// is movable
std::array<bool, 4> isMovableUpLeftDownRight()
{
    using Board::board;
    return {
        board->boardArrayIfUp() != board->boardArray(),
        board->boardArrayIfLeft() != board->boardArray(),
        board->boardArrayIfDown() != board->boardArray(),
        board->boardArrayIfRight() != board->boardArray(),
    };
}

PYBIND11_MODULE(game, m) {
    m.doc() = "2048 game interface";
    m.def("init_game", &initGame, "initialize the game");
    m.def("init_board", &initBoard, "initialize the board");
    m.def("print_result", &printResult, "print the average");
    m.def("exec_once", &execOnce, "align: up down left right");
    m.def("get_board", &getBoard, "get board state");
    m.def("is_movable_up_left_down_right", &isMovableUpLeftDownRight, "is movable up down left right");
}
