"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
def mc_trial(board, player):
    """
    Plays a random game (random moves) starting with given player and then alternating players.
    """
    # Populate until one wins
    while board.check_win() == None:
        # Player to play in one of ramaining empty squares (still playable)
        square_options = board.get_empty_squares()
        pick_square = random.choice(square_options)
        board.move(pick_square[0], pick_square[1], player)
        # Switch player for next move
        player = provided.switch_player(player)

    # print board
    # print board.check_win()
    

def mc_update_scores(scores,board,player):
    """
    Scores a completed board and update the scorse grid.
    """

    pass

def get_best_move(board,scores):
    """
    Finds all of the empty squares with the maximum score and randomly return one of them as a (row, column) tuple.
    It is an error to call this function with a board that has no empty squares as there is no possible next move.
    """
    # if board is not full

    return None

def mc_move(board,player,trials):
    """
    Uses the Monte Carlo simulation to return a move for the machine player in the form of a (row, column) tuple.
    """

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

board = provided.TTTBoard(3)
mc_trial(board, provided.PLAYERX)
# print board  