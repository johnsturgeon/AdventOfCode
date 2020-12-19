def wait_minutes(time_table):
    depart_time = int(time_table[0])
    all_busses = time_table[1].split(',')
    running_busses = []
    for bus in all_busses:
        if bus != 'x':
            running_busses.append(int(bus))

    wait_time = running_busses[0] - (depart_time % running_busses[0])
    earliest_bus = running_busses[0]
    for bus in running_busses:
        next_wait_time = bus - (depart_time % bus)
        if next_wait_time < wait_time:
            earliest_bus = bus
            wait_time = next_wait_time
    return wait_time * earliest_bus


def earliest_timestamp(time_table):
    all_busses = []
    slowest_bus_id = 0
    for index, bus in enumerate(time_table[1].split(',')):
        if bus != 'x':
            bus_id = int(bus)
            slowest_bus_id = max(slowest_bus_id, bus_id)
            all_busses.append({bus_id: index})
    while True:
        two_busses = {}
        two_busses.update(all_busses.pop(0))
        two_busses.update(all_busses.pop(0))
        earliest_time = earliest_time_for_two_busses(two_busses)
        if len(all_busses) > 0:
            all_busses.insert(0, {earliest_time: 0})
        else:
            return earliest_time


def earliest_time_for_two_busses(two_busses: dict):
    busses = []
    for bus in two_busses:
        busses.append(bus)
    less_frequent_bus = max(busses)
    more_frequent_bus = min(busses)
    less_freq_offset = two_busses[less_frequent_bus]
    more_freq_offset = two_busses[more_frequent_bus]
    diff_between_busses = less_freq_offset - more_freq_offset
    bus_depart_time = 0
    while True:
        bus_depart_time += less_frequent_bus
        slower_bus = bus_depart_time - diff_between_busses
        if slower_bus % more_frequent_bus == 0:
            return bus_depart_time - two_busses[less_frequent_bus]


#  Gave up, solution from:
#  https://dev.to/qviper/advent-of-code-2020-python-solution-day-13-24k4
def part2(data):
    busses = ["x" if x == "x" else int(x) for x in data[1].split(",")]
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    print(mods)
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val