import sys
from pathlib import Path

def rucksack_organization(file):
    """
    Every item type is identified by a single
    lowercase or uppercase letter (that is, a and
    A refer to different types of items).
    The list of items for each rucksack is given
    as characters all on a single line. A given
    rucksack always has the same number of items
    in each of its two compartments, so the first
    half of the characters represent items in the
    first compartment, while the second half of the
    characters represent items in the second compartment.
    To help prioritize item rearrangement, every item
    type can be converted to a priority:
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.


    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    """
    with open(file) as file:
        rucksack = file.split('\n')

    priority_count = 0

    # create a dictionary with corresponding keys and values to prioritize
    priorities = {}
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(letters)):
        priorities[letters[i]] = i + 1

    for compartments in rucksack:
        length = len(compartments)
        middle_index = length//2
        compartment1 = compartments[:middle_index]
        compartment2 = compartments[middle_index:]

        for character in compartment1:
            if character in compartment2:
                priority_count += priorities[character]
                break
    print(priority_count)
    return priority_count

# if __name__ == "__main__":
#     file = Path(sys.argv[1])
#     if Path.is_file(file):
#         rucksack_organization(Path.read_text(file))
#     else:
#         raise TypeError("This is not a file")