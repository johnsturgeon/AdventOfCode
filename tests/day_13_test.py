import pytest
import day_13


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_13.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_13.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_sample(sample_data):
    assert day_13.wait_minutes(sample_data) == 295
    assert day_13.part2(sample_data) == 1


def test_real(real_data):
    assert day_13.wait_minutes(real_data) == 156
    assert day_13.part2(real_data) == 404517869995362
