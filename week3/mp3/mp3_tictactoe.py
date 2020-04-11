"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided
# import mp3_testsuite

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10        # Number of trials to run
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

def mc_update_scores(scores, board, player):
    """
    Scores a completed board and update the scorse grid.
    """
    winner = board.check_win()
    board_dim = board.get_dim()
    other_player = provided.switch_player(player)

    # No need to check for draw to stop function as this already exists in provided.play_game()
    # Go through all squares in board
    for row in range(board_dim):
        for col in range(board_dim):
            if winner == player:
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == other_player:
                    scores[row][col] -= SCORE_OTHER
            elif winner == other_player:
                if board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                elif board.square(row, col) == other_player:
                    scores[row][col] += SCORE_OTHER

def get_best_move(board, scores):
    """
    Finds all of the empty squares with the maximum score and randomly return one of them as a (row, column) tuple.
    It is an error to call this function with a board that has no empty squares as there is no possible next move.
    """
    empty_sqrs = board.get_empty_squares()
    # "Pair" values and empty squares
    empty_scores = {}
    for sqr in empty_sqrs:
        empty_scores[sqr] = scores[sqr[0]][sqr[1]]  # sqr will always be unique as it's unique square among the empty ones

    # Get max score(s) among available    
    # No need for try - except as provided.play_game wouldn't call this if there are no more empty squares
    max_score = max(empty_scores.values())

    max_values = {}
    for (key, value) in empty_scores.items():
        if value == max_score:
            max_values[key] = value

    # Return random max value -if multiple- as (row, col)
    max_vals_keys = max_values.keys()
    highest_scoring_square = max_vals_keys[0]
    return highest_scoring_square

def mc_move(board, player, trials):
    """
    Uses the Monte Carlo simulation to return a move for the machine player in the form of a (row, column) tuple.
    """
    # Create scores list from scratch populated with 0s
    board_size = board.get_dim()
    scores_lst = [[0 for dummy_col in range(board_size)] for dummy_row in range(board_size)]

    for dummy in range(trials):
        # Create cloned board for this trial
        mc_board = board.clone()
    
        # Play a game
        mc_trial(mc_board, player)

        # Update score
        mc_update_scores(scores_lst, mc_board, player)

    # Return best possible move
    return get_best_move(board, scores_lst)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

# TESTS
# mp3_testsuite.run_suite(??)

# Check mc_trial
# board = provided.TTTBoard(3)
# mc_trial(board, provided.PLAYERX)
# print board
# Check mc_update_scores
# scores_lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# mc_update_scores(scores_lst, board, provided.PLAYERX)
# print scores_lst
# Check get_best_move
# added_scores = [[7.0, -2.0, 4.0], [0, 12.0, -6.0], [-1.0, -5.0, 11.0]]
# added_scores = [[7.0, 7.0, 7.0], [7.0, 7.0, 7.0], [7.0, 7.0, 7.0]]
# print get_best_move(board, added_scores)
# Check mc_move

# mc_move(board, provided.PLAYERX, NTRIALS)
