import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input: str) -> list[int]:
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def count_increases(readings: list[int]) -> int:
    # HACK: Set this to first reading, as it will equal no increase is counted
    previous_reading = readings[0]
    increases = 0
    for reading in readings:
        if reading > previous_reading:
            increases += 1
        previous_reading = reading
    return increases


def part1(data: list[int]) -> int:
    """Solve part 1"""
    return count_increases(data)


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
