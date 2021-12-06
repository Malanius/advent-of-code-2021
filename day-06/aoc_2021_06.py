import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input: str) -> list[int]:
    """Parse input"""
    splitted = puzzle_input.split(',')
    return [int(value) for value in splitted]


def part1(data: list[int]):
    """Solve part 1"""


def part2(data: list[int]):
    """Solve part 2"""


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
