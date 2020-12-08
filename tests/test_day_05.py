import pytest
import day_05


@pytest.fixture
def sample_data():
    return [
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL"
    ]


@pytest.fixture
def real_list():
    filename = "../data_for_day_05.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(line.rstrip())
    return real_list


def test_get_seat_id_sample(sample_data):
    assert day_05.get_seat_id(sample_data) == 820


def test_get_seat_id(real_list):
    assert day_05.get_seat_id(real_list) == 913
    assert day_05.get_seat_id(real_list, get_my_seat=True) == 717
