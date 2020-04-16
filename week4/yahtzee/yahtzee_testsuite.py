"""
Test suite for format function in Yahtzee
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    # Create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # Test reset function
    suite.run_test(len(game_class._grid),
        game_class._height,
        "Test reset() - height:")

    suite.report_results()
