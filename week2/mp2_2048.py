"""
Clone of 2048 game.
"""

# import poc_2048_testsuite
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
        self._height = grid_height
        self._width = grid_width

        # Create grid
        self.reset()

        # Precompute first indices of direction in one dictionary
        self._precomputed_indices = self.compute_first_indices()

    def compute_first_indices(self):
        """
        Computes the indices (as a touple) of the first row/column depending on direction
        """
        first_indices = {}

        # UP direction
        up_indices = []
        for index in range(self._width):
            # Create a tuple for indices
            index = (0, index)
            up_indices.append(index)

        # DOWN direction
        down_indices = []
        for index in range(self._width):
            # Create a tuple for indices
            index = (self._height - 1, index)
            down_indices.append(index)

        # LEFT direction
        left_indices = []
        for index in range(self._height):
            # Create a tuple for indices
            index = (index, 0)
            left_indices.append(index)

        # RIGHT direction
        right_indices = []
        for index in range(self._height):
            # Create a tuple for indices
            index = (index, self._width - 1)
            right_indices.append(index)

        first_indices[RIGHT] = right_indices
        first_indices[LEFT] = left_indices
        first_indices[DOWN] = down_indices
        first_indices[UP] = up_indices

        return first_indices

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = []
        for dummy_row in range(self._height):
            row = []
            self._grid.append(row)
            for dummy_cell in range(self._width):
                row.append(0)

        for dummy_i in range(2):
            self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str_grid = ""

        for row in range(self._height):
            line = self._grid[row]
            for cell in range(self._width):
                if cell < self._width - 1:
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
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_indices_list = self._precomputed_indices[direction]
        offset = OFFSETS[direction]

        # Loop all cells in row/column starting from initial indices
        for tpl in initial_indices_list:
            # Build temporary list in that direction
            tile_values = []
            tlps_list = []
            if direction == UP or direction == DOWN:
                # Loop through height of column
                for col in range(self._height):
                    # At each iteration move in direction of offset
                    offset_tpl = tuple([col * x for x in offset])
                    index_tpl = tuple(map(sum, zip(tpl, offset_tpl)))
                    # Save index to recompose grid at the end
                    tlps_list.append(index_tpl)
                    # Add number found in grid at that index
                    tile_values.append(self._grid[index_tpl[0]][index_tpl[1]])
            else:
                # Loop through width of row
                for row in range(self._width):
                    offset_tpl = tuple([row * x for x in offset])
                    index_tpl = tuple(map(sum, zip(tpl, offset_tpl)))
                    tlps_list.append(index_tpl)
                    tile_values.append(self._grid[index_tpl[0]][index_tpl[1]])
            merged_tiles = merge(tile_values)
            for index in range(len(merged_tiles)):
                self._grid[tlps_list[index][0]][tlps_list[index][1]] = merged_tiles[index]


        # TEMP for testing
        # return self._grid


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
        if self._grid[row_index][col_index] == 0:
            self._grid[row_index][col_index] = tile

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """

        return self._grid[row][col]

# poc_2048_testsuite.run_suite(TwentyFortyEight(4, 6))
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
