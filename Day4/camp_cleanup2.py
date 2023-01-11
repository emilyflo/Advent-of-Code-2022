from pathlib import Path
import sys

def camp_cleanup2(file_name):
    """
    given two elves' section assignments, compare their sections
    and check if there are any overlapping values.
    return the sum of assignment pairs that fully contain the other.
    """

    overlapping_pairs = 0

    section_assignments = read_file(file_name).split('\n')


    for pairs in range(len(section_assignments)):
        section_assignments[pairs] = section_assignments[pairs].replace(',',' ').replace('-',' ').split()
        section_assignments[pairs] = list(map(int,section_assignments[pairs]))

        if section_assignments[pairs][0] <= section_assignments[pairs][2] and section_assignments[pairs][1] <= section_assignments[pairs][3]:
            overlapping_pairs += 1
        elif section_assignments[pairs][0] >= section_assignments[pairs][2] and section_assignments[pairs][1] >= section_assignments[pairs][3]: 
            overlapping_pairs += 1

    print(overlapping_pairs)
    return overlapping_pairs

def read_file(file_name):
    file = Path(file_name)
    if Path.is_file(file):
        return Path.read_text(file)
    else:
        raise TypeError("This is not a file")

if __name__ == "__main__":
    camp_cleanup2(sys.argv[1])
