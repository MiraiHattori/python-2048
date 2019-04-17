#pragma once
#include "board/board.hpp"
#include <iomanip>

namespace Game
{

class Game
{
public:
    explicit Game()
    {
        this->init();
    }

    void init()
    {
        Board::board = std::make_unique<Board::Board<ROW_SIZE, COL_SIZE>>();
        Board::board->init();
    }

    void execOnce(std::string command)
    {
        using Board::board;
        bool to_stop = false;

        // board->boardArray()で、2048の現在の盤面がstd::array<std::array<int, COL_SIZE>, ROW_SIZE>で返ってきます
        if /* constexpr */ (Params::PRINT_BOARD) { for (const auto& row : board->boardArray()) {
                for (const auto& cell : row) {
                    std::cout << std::fixed
                              << std::setw(Params::MAX_DIGIT_TO_SHOW) << (cell == 0 ? 0 : Util::power(2u, static_cast<unsigned int>(cell)));
                }
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }
        if /* constexpr */ (Params::PRINT_TURN) {
            std::cout << "turn: " << board->turn() << std::endl;
        }
        if /* constexpr */ (Params::PRINT_SCORE) {
            std::cout << "score: " << board->score() << std::endl;
        }

        //  // commandを利用
        //  if (board->boardArrayIfUp() != board->boardArray()) {
        //      board->up();
        //  } else {
        //      if (board->boardArrayIfLeft() != board->boardArray()) {
        //          board->left();
        //      } else {
        //          if (board->boardArrayIfDown() != board->boardArray()) {
        //              board->down();
        //          } else {
        //              board->right();
        //          }
        //      }
        //  }
        if (command == "up") {
            board->up();
        } else if (command == "down") {
            board->down();
        } else if (command == "left") {
            board->left();
        } else if (command == "right") {
            board->right();
        } else if (command == "quit") {
            board->quit();
        } else {
            std::cout << "command is " << command << ". game is over. is it typo?" << std::endl;
            m_game_iteration++;
            board->clear();
            return;
        }
        // 選択された動作に基づいて実際に盤面を上下左右動かし、ターンや点数を更新する
        if (not board->move()) {
            if /* constexpr */ (Params::PRINT_GAMEOVER) {
                std::cout << "Invalid Move. Game Over." << std::endl;
            }
            if /* constexpr */ (Params::PRINT_RESULT) {
                std::cout << "Turn: " << board->turn()
                          << " Score: " << board->score() << std::endl;
            }
            m_turns.emplace_back(board->turn());
            m_scores.emplace_back(board->score());
            to_stop = true;
        }
        // 2か4を盤面に加える
        if (not board->placeTwoOrFour()) {
            if /* constexpr */ (Params::PRINT_GAMEOVER) {
                std::cout << "No space left. Game Over." << std::endl;
            }
            if /* constexpr */ (Params::PRINT_RESULT) {
                std::cout << "Turn: " << board->turn()
                          << " Score: " << board->score() << std::endl;
            }
            m_turns.emplace_back(board->turn());
            m_scores.emplace_back(board->score());
            to_stop = true;
        }
        // 盤面を動かすとどうなるか先行評価
        board->eagerMoveEvaluation();
        if (to_stop) {
            m_game_iteration++;
            board->clear();
        }
    }

    void printResult()
    {
        std::cout << "Total iteration: " << m_game_iteration << std::endl;
        std::cout << "Turn average: "
                  << static_cast<double>(std::accumulate(m_turns.begin(), m_turns.end(), 0))
                         / m_turns.size()
                  << std::endl;
        std::cout << "Score average: "
                  << static_cast<double>(std::accumulate(m_scores.begin(), m_scores.end(), 0))
                         / m_scores.size()
                  << std::endl;
    }

private:
    int m_game_iteration{};
    std::vector<int> m_turns{};
    std::vector<int> m_scores{};
};

extern std::unique_ptr<Game> game;

} // namespace Game
