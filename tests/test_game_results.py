import numpy as np

from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.games.examples.tictactoe import TicTacToeGameState


# O 表示空地
# D 砖石
# G 黄金
# H 障碍物
# A A玩家
# B B玩家


def test_if_initial_state_no_result():
    state = TicTacToeGameState(np.zeros((3, 3)), next_to_move=1)
    assert state.game_result is None


def test_if_1_wins_diagonal_case1():
    gamestate = -np.ones((3, 3))
    gamestate[0, 0] = 1
    gamestate[1, 1] = 1
    gamestate[2, 2] = 1

    state = TicTacToeGameState(gamestate, next_to_move=-1)
    assert state.game_result == 1


def test_if_1_wins_diagonal_case2():
    gamestate = -np.ones((3, 3))
    gamestate[0, 2] = 1
    gamestate[1, 1] = 1
    gamestate[2, 0] = 1

    state = TicTacToeGameState(gamestate, next_to_move=-1)
    assert state.game_result == 1


def test_if_0_wins_diagonal_case1():
    gamestate = np.ones((3, 3))
    gamestate[0, 2] = -1
    gamestate[1, 1] = -1
    gamestate[2, 0] = -1


def test_if_0_wins_diagonal_case2():
    gamestate = np.ones((3, 3))
    gamestate[0, 0] = -1
    gamestate[1, 1] = -1
    gamestate[2, 2] = -1

    state = TicTacToeGameState(gamestate, next_to_move=1)
    assert state.game_result == -1


def test_tic_tac_toe_best_action():
    state = np.zeros((3, 3))
    initial_board_state = TicTacToeGameState(state=state, next_to_move=1)

    root = TwoPlayersGameMonteCarloTreeSearchNode(state=initial_board_state,
                                                  parent=None)
    mcts = MonteCarloTreeSearch(root)
    return mcts.best_action(1000)


if __name__ == "__main__":
    best_node = test_tic_tac_toe_best_action()
    for node in best_node.children:
        print(node.q)
        print(node.state.runningx,node.state.runningy)