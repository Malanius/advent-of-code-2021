import pathlib
from typing import List, TypedDict


import pandas as pd

PUZZLE_DIR = pathlib.Path(__file__).parent


class BitCount(TypedDict):
    zeroes: int
    ones: int


def get_bit_counts(data: list[list[str]]) -> list[BitCount]:
    df = pd.DataFrame(data)
    bit_counts: BitCount = []
    for column in df:
        counts = df[column].value_counts()
        bit_counts.append({"zeroes": counts["0"], "ones": counts["1"]})
    return bit_counts


def parse(puzzle_input: str):
    """Parse input"""
    lines = puzzle_input.splitlines()
    data = [list(line) for line in lines]
    return data

def part1(data):
def part1(data: list[list[str]]):
    """Solve part 1"""
    bit_counts = get_bit_counts(data)


def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
