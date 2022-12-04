import sys
from pathlib import Path

def elf_tournament(file):
    """
    Rock Paper Scissors is a game between two players.
    Each game contains many rounds; in each round,
    the players each simultaneously choose one of Rock,
    Paper, or Scissors using a hand shape. Then, a winner
    for that round is selected: Rock defeats Scissors,
    Scissors defeats Paper, and Paper defeats Rock.
    If both players choose the same shape, the round
    instead ends in a draw.

    A - rock
    B - paper
    C - scissors
    X - rock
    Y - paper
    Z - scissors

    The winner of the whole tournament is the player
    with the highest score. Your total score is the sum
    of your scores for each round. The score for a single
    round is the score for the shape you selected
    (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round
    (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    line = file.split('\n')

    score = 0

    win = 6
    lose = 0
    draw = 3

    rock = 1
    paper = 2
    scissors = 3

    round = {
        'A X' : draw + rock,
        'A Y' : win + paper,
        'A Z' : lose + scissors,
        'B X' : lose + rock,
        'B Y' : draw + paper,
        'B Z' : win + scissors,
        'C X' : win + rock,
        'C Y' : lose + paper,
        'C Z' : draw + scissors,
    }

    for element in line:
        score += round[element]
    
    print(score)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        elf_tournament(Path.read_text(file))
    else:
        raise TypeError("This is not a file")