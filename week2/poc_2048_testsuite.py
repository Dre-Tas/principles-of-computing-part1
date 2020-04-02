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
    suite.run_test(len(game_class._grid),
        game_class._height,
        "Test reset() - height:")

    suite.run_test(len(game_class._grid[0]),
        game_class._width,
        "Test reset() - height:")

    suite.run_test(sum([len(cell) for cell in game_class._grid]),
        game_class.get_grid_height() * game_class.get_grid_width(),
        "Test reset() - cells:")

    suite.run_test(game_class._grid[0][0], 0, "Test reset() - cell:")

    # Test new_tile function

    # Check that the tiles have been created
    # by checking that there aren't only 0 tiles
    sum_of_tiles = 0
    for row in game_class._grid:
        for cell in row:
            sum_of_tiles += cell

    suite.run_test(True if sum_of_tiles > 2 else False,
        True,
        "Test new_tile() - zero cells:")

    # Test _str_
    suite.run_test(type(game_class.__str__()),
        str,
        "Test __str__() - str returns string:")

    nums_list = []
    for char in game_class.__str__():
        if char.isdigit():
            nums_list.append(char)

    suite.run_test(True if 2 or 4 in nums_list else False,
    True,
    "Test __str__() -  only contains 2s and 4s:")

    non_zeros = 0
    for elem in nums_list:
        if int(elem) is not 0:
            non_zeros += 1

    suite.run_test(True if non_zeros == 2 else False,
    True,
    "Test __str__() - has 2 non zero items:")

    # # Test directions dictionary
    # list_of_row_index = []
    # for i in game_class.move("DOWN"):
    #     list_of_row_index.append(i[0])
    
    # suite.run_test(True if all((game_class._height - 1) for x in list_of_row_index) else False,
    #     True,
    #     "Test move() - row index is 3:")

    # list_of_col_index = []
    # for i in game_class.move("RIGHT"):
    #     list_of_col_index.append(i[0])
    
    # suite.run_test(True if all((game_class._width - 1) for x in list_of_col_index) else False,
    #     True,
    #     "Test move() - col index is 3:")

    # Directions, DO NOT MODIFY
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    print game_class.__str__()
    print game_class.move(UP)
    
    suite.report_results()
  