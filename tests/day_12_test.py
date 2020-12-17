import pytest
import day_12


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_12.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_12.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_sample(sample_data):
    assert day_12.get_manhattan_distance(sample_data) == 25
    assert day_12.get_manhattan_distance(sample_data, use_waypoint=True) == 286


def test_real(real_data):
    assert day_12.get_manhattan_distance(real_data) == 590
    assert day_12.get_manhattan_distance(real_data, use_waypoint=True) == 42013
