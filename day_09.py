def get_invalid_cipher(cipher_data, preamble_length):
    preamble_shift = 0
    for n in range(preamble_length, len(cipher_data)):
        preamble = cipher_data[preamble_shift:preamble_length+preamble_shift]
        num_to_check = cipher_data[n]
        if can_sum_two(preamble, num_to_check):
            preamble_shift += 1
        else:
            return num_to_check


def get_weakness(cipher_data, preamble_length):
    invalid_cipher = get_invalid_cipher(cipher_data, preamble_length)
    i = 0
    sum_of_nums = 0
    last_num_in_range = 0
    while sum_of_nums != invalid_cipher:
        sum_of_nums = 0
        for n in range(i, len(cipher_data)):
            last_num_in_range = n
            sum_of_nums += cipher_data[n]
            if sum_of_nums >= invalid_cipher:
                break
        i += 1
    i -= 1  # back the counter up one since it advanced
    last_num_in_range += 1
    range_of_nums = cipher_data[i:last_num_in_range]
    sum = 0
    for num in range_of_nums:
        print(num)
        sum += num
    print(sum)
    return sorted(range_of_nums)[0] + sorted(range_of_nums)[-1]


def can_sum_two(input_set: list, input_number: int):
    for num in input_set:
        for n in range(0, len(input_set)):
            if num != input_set[n]:
                if num + input_set[n] == input_number:
                    return True
    return False
