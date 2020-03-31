"""
Merge function for 2048 game.
"""

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
    Function that merges a single row or column in 2048.
    """

    ordered_line = push_zeros(line)

    # Sum consecutive equal numbers
    for index in range(len(ordered_line) - 1):
        if ordered_line[index] == ordered_line[index + 1]:
            ordered_line[index] = ordered_line[index] * 2
            ordered_line[index + 1] = 0

    return push_zeros(ordered_line)

print(merge([8,8]))
print(merge([2,0,2,4]))
print(merge([0,0,2,2]))
print(merge([2,2,0,0]))
print(merge([2,2,2,2,2]))
print(merge([8,16,16,8]))

print(merge([4, 4, 8, 8]))
