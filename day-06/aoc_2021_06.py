import pathlib
import time

import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input: str) -> list[int]:
    """Parse input"""
    splitted = puzzle_input.split(',')
    return [int(value) for value in splitted]


# Not fastest way to run, but write, let's hope part 2 is not for more days...
def part1(data: list[int], days: int) -> int:
    """Solve part 1"""
    start = time.perf_counter()
    for i in range(0, days):
        # print(f"Day {i:>2}: {data}")
        new_data: list[int] = []
        births: list[int] = []
        for fish_timer in data:
            if fish_timer == 0:
                new_data.append(6)
                births.append(8)
                continue
            timer = fish_timer - 1
            new_data.append(timer)
        data = new_data + births
    end = time.perf_counter()
    print(f"Solved {days} days in {end - start:0.4f} seconds")
    return len(data)


def part2(data: list[int], days: int):
    """Solve part 2"""
    data_np = np.array(data)
    start = time.perf_counter()
    for i in range(0, days):
        if (i % 32 == 0):
            print(f"Day {i:>2}: {data_np}")
        births = (data_np == 0).sum()
        ones = np.ones(data_np.size, dtype=int)
        new_data: np.ndarray = data_np - ones
        new_data = np.concatenate((new_data, np.full(births, 8)))
        new_data = np.where(new_data < 0, 6, new_data)
        data_np = new_data
    end = time.perf_counter()
    print(f"Solved {days} days in {end - start:0.4f} seconds")
    return len(data_np)


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, days=80)
    solution2 = part2(data, days=256)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
