import pytest
import day_06


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_06.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_06.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_get_seat_id_sample(sample_data):
    assert day_06.get_sum_of_answers(sample_data) == 11
    assert day_06.get_intersection_of_answers(sample_data) == 6


def test_get_seat_id(real_data):
    assert day_06.get_sum_of_answers(real_data) == 6297
    assert day_06.get_intersection_of_answers(real_data) == 3158
