"""
Test suite for format function in "Stopwatch - The game"
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    # Create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # Test reset function
    suite.run_test(len(game_class.reset()),
        game_class.height,
        "Test reset() - height:")

    suite.run_test(len(game_class.reset()[0]),
        game_class.width,
        "Test reset() - height:")

    suite.run_test(sum([len(cell) for cell in game_class.reset()]),
        game_class.get_grid_height() * game_class.get_grid_width(),
        "Test reset() - cells:")

    suite.run_test(game_class.reset()[0][0], 0, "Test reset() - cell:")

    # Test new_tile function

    # Check that the tiles have been created
    # by checking that there aren't only 0 tiles
    sum_of_tiles = 0
    for row in game_class.grid:
        for cell in row:
            sum_of_tiles += cell

    suite.run_test(True if sum_of_tiles > 2 else False,
        True,
        "Test new_tile() - zero cells:")

    
    suite.report_results()
  