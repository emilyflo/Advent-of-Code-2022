from pathlib import Path
import sys
from string import ascii_letters
from rucksack import read_file


def elf_badges(file_name):
    """
    every 3 lines is a group of 3 elves
    every 3 lines will share one common character
    assign a value to that character
    add each shared value into the badge_priorities count
    return the sum of the badge priorities
    """
    data = read_file(file_name).split()

    badge_priorities = 0

    for line in range(0, len(data), 3):
        for letter in data[line]:
            if letter in data[line + 1] and letter in data[line + 2]:
                badge_priorities += get_character_priority(letter)
                break
    return badge_priorities 
        
def get_character_priority(character):
    return ascii_letters.index(character) + 1

print("this is day 3 part 2's solution:", elf_badges('input.txt'))




def read_file(file_name):
    file = Path(file_name)
    if Path.is_file(file):
        return Path.read_text(file)
    else:
        raise TypeError("This is not a file")

# if __name__ == "__main__":
#     elf_badges(sys.argv[1])