from math import prod


def sum_two(list_of_numbers):
    length_of_list = len(list_of_numbers)
    for number in list_of_numbers:
        for i in range(0,length_of_list):
            if number + list_of_numbers[i] == 2020:
                return number * list_of_numbers[i]


def sum_three(list_of_numbers):
    length_of_list = len(list_of_numbers)
    for first_number in list_of_numbers:
        for i in range(0,length_of_list):
            second_number = list_of_numbers[i]
            for i in range(0,length_of_list):
                if sum([first_number, second_number, list_of_numbers[i]]) == 2020:
                    return prod([first_number, second_number, list_of_numbers[i]])
