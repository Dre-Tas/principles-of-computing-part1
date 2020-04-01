"""
Clone of 2048 game.
"""

import poc_2048_testsuite
#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

# Other global variables
PROBABILITY_OF_TWO = 0.9  # probability to pick 2

def push_zeros(lst):
    """
    Push 0s to the end of the list
    """

    zeros = []
    push_lst = []

    for cell in lst:
        if cell == 0:
            zeros.append(0)
        else:
            push_lst.append(cell)

    for zero in zeros:
        push_lst.append(zero)

    return push_lst

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    ordered_line = push_zeros(line)

    # Sum consecutive equal numbers
    for index in range(len(ordered_line) - 1):
        if ordered_line[index] == ordered_line[index + 1]:
            ordered_line[index] = ordered_line[index] * 2
            ordered_line[index + 1] = 0

    return push_zeros(ordered_line)

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # Store height and width
        self.height = grid_height
        self.width = grid_width

        # Create grid
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = []
        for dummy_row in range(self.height):
            row = []
            self.grid.append(row)
            for dummy_cell in range(self.width):
                row.append(0)

        for dummy_i in range(2):
            self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str_grid = ""

        for row in range(self.height):
            line = self.grid[row]
            for cell in range(self.width):
                if cell < self.width - 1:
                    str_grid += str(line[cell]) + ", "
                else:
                    str_grid += str(line[cell])
            str_grid += "\n"
        
        # print str_grid
        return str_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Create tile randomly
        tile = None
        if random.random() < PROBABILITY_OF_TWO:
            tile = 2
        else:
            tile = 4

        # Pick location of tile in grid
        row_index = random.randrange(0, self.get_grid_height(), 1)
        col_index = random.randrange(0, self.get_grid_width(), 1)

        # Make sure I'm not selecting the same tile twice
        if self.grid[row_index][col_index] == 0:
            self.grid[row_index][col_index] = tile

        pass

    # def set_tile(self, row, col, value):
    #     """
    #     Set the tile at position row, col to have the given value.
    #     """
    #     # replace with your code
    #     pass

    # def get_tile(self, row, col):
    #     """
    #     Return the value of the tile at position row, col.
    #     """
    #     # replace with your code
    #     return 0

poc_2048_testsuite.run_suite(TwentyFortyEight(4, 6))
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
