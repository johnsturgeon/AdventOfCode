import pytest
import day_08


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_08.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_08.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_sample(sample_data):
    assert day_08.value_before_loop(sample_data) == 5
    assert day_08.value_before_loop(sample_data, rewrite_code=True) == 8


def test_real(real_data):
    assert day_08.value_before_loop(real_data) == 2025
    assert day_08.value_before_loop(real_data, rewrite_code=True) == 2001
