import sys
from pathlib import Path
from string import ascii_letters

def rucksack_organization(file_name):
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

    rucksack = read_file(file_name).split('\n')

    priority_count = 0

    for compartments in rucksack:
        compartment1, compartment2 = split_compartments(compartments)
        character = find_similiar_character(compartment1, compartment2)
        priority_count += get_character_priority(character)


    return priority_count

    # priority_count = 0

    # for compartments in rucksack:
    #     length = len(compartments)
    #     middle_index = length//2
    #     compartment1 = compartments[:middle_index]
    #     compartment2 = compartments[middle_index:]

    #     for character in compartment1:
    #         if character in compartment2:
    #             priority_count += ascii_letters.index(character) + 1
    #             break
    # print(priority_count)
    # return priority_count

def find_similiar_character(list_1, list_2):
    """
    what this does
    Example:
        find_similiar_character([1,2,3], [3,4,5]) => 3
    """
    for character in list_1:
        if character in list_2:
            return character
    # return (set(list_1) & set(list_2)).pop()

def get_character_priority(character):
    return ascii_letters.index(character) + 1

def split_compartments(compartments):
    length = len(compartments)
    middle_index = length//2
    compartment1 = compartments[:middle_index]
    compartment2 = compartments[middle_index:]
    return compartment1, compartment2



def read_file(file_name):
    file = Path(file_name)
    if Path.is_file(file):
        return Path.read_text(file)
    else:
        raise TypeError("This is not a file")

print("this is Day 3 part 1's solution:", rucksack_organization('input.txt'))
# if __name__ == "__main__":
#     rucksack_organization(sys.argv[1])