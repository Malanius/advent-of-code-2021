import pathlib
import pytest
import aoc_2021_03 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == [
        ['0', '0', '1', '0', '0'],
        ['1', '1', '1', '1', '0'],
        ['1', '0', '1', '1', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '0', '1', '0', '1'],
        ['0', '1', '1', '1', '1'],
        ['0', '0', '1', '1', '1'],
        ['1', '1', '1', '0', '0'],
        ['1', '0', '0', '0', '0'],
        ['1', '1', '0', '0', '1'],
        ['0', '0', '0', '1', '0'],
        ['0', '1', '0', '1', '0'],
    ]


def test_part1(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 198


def test_part2_example2(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 230
