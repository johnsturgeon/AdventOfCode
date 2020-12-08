import pytest
import day_03


@pytest.fixture
def sample_data():
    return [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"
    ]


@pytest.fixture
def real_list():
    filename = "../data_for_day_03.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_trees_hit_sample(sample_data):
    assert day_03.trees_hit(sample_data, increment_x=3, increment_y=1) == 7
    assert day_03.product_trees_hit(sample_data) == 336


def test_trees_hit(real_list):
    assert day_03.trees_hit(real_list, increment_x=3, increment_y=1) == 169
    assert day_03.product_trees_hit(real_list) == 7560370818
