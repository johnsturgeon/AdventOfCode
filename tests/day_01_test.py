import pytest
import day_01


@pytest.fixture
def sample_list():
    return [1721,
            979,
            366,
            299,
            675,
            1456]


@pytest.fixture
def real_list():
    filename = "../data_for_day_01.txt"
    real_list = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            real_list.append(int(line))
    return real_list


def test_day_01_sample(sample_list):
    assert day_01.sum_two(sample_list) == 514579
    assert day_01.sum_three(sample_list) == 241861950

#
def test_day_01(real_list):
    assert day_01.sum_two(real_list) == 1019571
    assert day_01.sum_three(real_list) == 100655544
