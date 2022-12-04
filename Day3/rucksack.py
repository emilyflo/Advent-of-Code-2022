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

    rucksack = file.split('\n')

    # iterate through each line - cut line in half and find the common character in both halves
    # if it's a lowercase character, assign it its value 1-26 depending on where it is in the alphabet
    # if it's an uppercase character, assign it its value 27-52 depending on where it is in the alphabet (n + 26)
    # when the end of the input list is reached, find the sum each line value
    # a 1, b 2, c 3, d 4, e 5, f 6, g 7, h 8, i 9, j 10, k 11, l 12, m 13, n 14, o 15, p 16, q 17, r 18, s 19, t 20, u 21, v 22, w 23, x 24, y 25, z 26
    # A 27, B 28, C 29, D 30, E 31, F 32, G 33, H 34, I 35, J 36, K 37, L 38, M 39, N 40, O 41, P 42, Q 43, R 44, S 45, T 46, U 47, V 48, W 49, X 50, Y 51, Z 52
    priority_count = 0

    for compartments in rucksack:
        # divide rucksack in two
        # if same character in both, find if it's upper or lowercase
        # attach correct value
        # continue
        # sum(rucksack)

        lowercase = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26
        }
        
        uppercase = {
            'A': 27,
            'B': 28,
            'C': 29,
            'D': 30,
            'E': 31,
            'F': 32,
            'G': 33,
            'H': 34,
            'I': 35,
            'J': 36,
            'K': 37,
            'L': 38,
            'M': 39,
            'N': 40,
            'O': 41,
            'P': 42,
            'Q': 43,
            'R': 44,
            'S': 45,
            'T': 46,
            'U': 47,
            'V': 48,
            'W': 49,
            'X': 50,
            'Y': 51,
            'Z': 52
        }

        length = len(compartments)
        middle_index = length//2
        compartment1 = compartments[:middle_index]
        compartment2 = compartments[middle_index:]
        # print(compartment1)
        # print(compartment2)
        for character in compartment1:
            if character in compartment2:
                # print(character)
                if character in lowercase:
                    # add that value to += priority_count
                # if character in uppercase:
                    print('duplicate character!')
                    # add that value to += priority_count
                    continue
            # sum(priority_count)
            print(priority_count)
        

        # print(rucksack)

if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        rucksack_organization(Path.read_text(file))
    else:
        raise TypeError("This is not a file")