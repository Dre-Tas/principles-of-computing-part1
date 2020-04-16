"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# # Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

# import yahtzee_testsuite

from collections import Counter

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    # Group items in list by value
    counter = Counter(hand)
    grouped = [[k,]*v for k,v in counter.items()]

    # Sum all sublists
    sums = []
    for lst in (grouped):
        sums.append(sum(lst))

    # Return max value
    return sorted(sums)[-1]

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # Generate all possible sequences with free dice and held dice
    free_sequences = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    all_sequences = [tup + held_dice for tup in free_sequences]
    # print added_lst

    # Probablity of each sequence
    sequence_probability = 1 / float(len(all_sequences))

    # Get score for each dice combination
    scored_seqs = [score(tpl) for tpl in all_sequences]

    value = sequence_probability * sum([x for x in scored_seqs])

    return value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    # Initialise reult with empty tuple (always present)
    all_holds = set([()])

    # Remove combinations of the hand
    for item in range(len(hand)):
        idc_to_remove = gen_all_sequences(range(len(hand)), item)
        for idc in idc_to_remove:
            hand_lst = list(hand)

            # Delete elements at indices
            for idx in idc:
                hand_lst[idx] = None
            for dummy in range(hand_lst.count(None)):
                hand_lst.remove(None)

            all_holds.add(tuple(hand_lst))

    return all_holds

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
# run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
# yahtzee_testsuite.run_suite()
print score((6, 1, 1, 1, 5))
print score((2, 2, 2, 4, 4, 5, 6))
print expected_value((2, 2), 6, 2)
print gen_all_holds((1, 1, 5))
# print gen_all_holds((1, 1, 1, 5, 6))
