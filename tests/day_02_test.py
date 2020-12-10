import pytest
import day_02


@pytest.fixture
def sample_data():
    return [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]


@pytest.fixture
def real_list():
    filename = "../data_for_day_02.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_day_02_sample(sample_data):
    assert day_02.count_valid_passwords_by_occurrence(sample_data) == 2
    assert day_02.count_valid_passwords_by_position(sample_data) == 1


def test_day_02(real_list):
    assert day_02.count_valid_passwords_by_occurrence(real_list) == 591
    assert day_02.count_valid_passwords_by_position(real_list) == 335
