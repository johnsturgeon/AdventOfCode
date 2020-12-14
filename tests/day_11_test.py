import pytest
import day_11


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_11.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            stripped_line = line.rstrip()
            line_list = []
            for c in stripped_line:
                line_list.append(c)
            real_list.append(line_list)
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_11.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            stripped_line = line.rstrip()
            line_list = []
            for c in stripped_line:
                line_list.append(c)
            real_list.append(line_list)
    return real_list


def test_sample(sample_data):
    assert day_11.sit_passengers(sample_data) == 37


def test_sample_far(sample_data):
    assert day_11.sit_passengers_far(sample_data) == 26


def test_real(real_data):
    assert day_11.sit_passengers(real_data) == 2204


def test_real_far(real_data):
    assert day_11.sit_passengers_far(real_data) == 1986
