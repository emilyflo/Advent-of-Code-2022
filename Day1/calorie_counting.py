def hostess_with_the_mostess(file):
    """
    Iterate through input.txt to find how many
    calories that the Elf with the most calories
    has in his magical snack bag.
    """
    with open(file) as file:

        calorie_count = 0
        mostess = []

        for line in file:
            if len(line.strip()) != 0:
                calorie_count += int(line)
                continue
            mostess.append(calorie_count)
            calorie_count = 0

    mostess.sort(reverse=True)
    
    print(sum(mostess[:3]))
    print(mostess[0])
    return mostess

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Find how many calories the Elf with the most calories has.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        hostess_with_the_mostess(file)
    else:
        print(f"{file} does not exist!")
        exit(1)