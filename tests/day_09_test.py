import pytest
import day_09


@pytest.fixture
def sample_data():
    filename = "../sample_data_day_09.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(int(line.rstrip()))
    return real_list


@pytest.fixture
def real_data():
    filename = "../data_for_day_09.txt"
    real_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            real_list.append(int(line.rstrip()))
    return real_list


def test_sample(sample_data):
    assert day_09.get_invalid_cipher(sample_data, preamble_length=5) == 127
    assert day_09.get_weakness(sample_data, preamble_length=5) == 62


def test_real(real_data):
    assert day_09.get_invalid_cipher(real_data, preamble_length=25) == 32321523
    assert day_09.get_weakness(real_data, preamble_length=25) == 4794981
