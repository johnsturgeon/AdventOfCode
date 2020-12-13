import math


def my_joltage(adapters):
    return sorted(adapters)[-1] + 3


def count_jolt_difference(adapters, distance):
    count = 0
    sorted_adapters = sorted(adapters)
    for i, adapter in enumerate(sorted_adapters):
        if i < len(adapters) - 1:
            if abs(adapter - sorted_adapters[i+1]) == distance:
                if count:
                    count += 1
                else:
                    # always count two for the first adapter.. self, and lookahead both count
                    count += 2
    return count


def get_mask_for_num(length, number):
    max_combinations = 2**length
    len_mask = len(str(bin(max_combinations))[2:]) - 1
    mask = []
    bin_mask = bin(number)[2:]
    for c in bin_mask:
        mask.append(int(c))
    pad_length = len_mask - len(mask)
    for i in range(0, pad_length):
        mask.insert(0, 0)
    return mask


def count_paths_through_adapters(length):
    assert length > 0
    max_combinations = 2**length
    valid_path_count = 0
    for i in range(0, max_combinations):
        mask = get_mask_for_num(length, i)
        distance = 0
        valid_path = True
        for n in mask:
            if n == 0:
                distance += 1
                if distance >= 3:
                    valid_path = False
                    break
            elif n == 1:
                distance = 0
        if valid_path:
            valid_path_count += 1
    return valid_path_count


def count_all_combinations(adapters):
    sorted_adapters = sorted(adapters)
    i = 0
    prev_adapter = 0
    adapter_gap_counts = []
    chain = -1
    for adapter in sorted_adapters:
        if adapter - prev_adapter == 1:
            chain += 1
        else:
            if chain >= 1:
                adapter_gap_counts.append(count_paths_through_adapters(chain))
            chain = -1
        prev_adapter = adapter
    # add last chain
    if chain >= 1:
        adapter_gap_counts.append(count_paths_through_adapters(chain))
    return math.prod(adapter_gap_counts)


def multiply_differences(adapters):
    return count_jolt_difference(adapters, 1) * count_jolt_difference(adapters, 3)
