import numpy as np

from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.games.examples.tictactoe import TicTacToeGameState


def test_tic_tac_toe_best_action():
    state = np.zeros((10, 10))
    initial_board_state = TicTacToeGameState(state=state, next_to_move=1)

    root = TwoPlayersGameMonteCarloTreeSearchNode(state=initial_board_state,
                                                  parent=None)
    mcts = MonteCarloTreeSearch(root)
    return mcts.best_action(1000)


if __name__ == "__main__":
    best_node = test_tic_tac_toe_best_action()
    for node in best_node.children:
        print(node.q)
        print(node.state.runningx, node.state.runningy)
