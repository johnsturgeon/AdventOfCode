import pytest
import day_10


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_10.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(int(line.rstrip()))
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_10.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(int(line.rstrip()))
    return real_list


def test_sample(sample_data):
    assert day_10.multiply_differences(sample_data) == 220
    assert day_10.count_all_combinations(sample_data) == 19208


def test_real(real_data):
    assert day_10.multiply_differences(real_data) == 2450
    assert day_10.count_all_combinations(real_data) == 32396521357312
