import pytest
import day_07


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_07.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_07.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_get_seat_id_sample(sample_data):
    assert day_07.get_parent_bags(sample_data, 'shiny gold') == 4
    assert day_07.number_of_contained_bags(sample_data, 'shiny gold') == 32


def test_get_seat_id(real_data):
    assert day_07.get_parent_bags(real_data, 'shiny gold') == 32
