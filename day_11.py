import copy


def seat_is_ok_to_sit(seats: list[str], row: int, column: int):
    adj_seats = occupied_adjacent_seats(seats, row, column)
    seat = seats[row][column]
    if seat == 'L' and adj_seats == 0:
        return True
    elif seat == '#' and adj_seats < 4:
        return True
    else:
        return False


def seat_is_ok_to_sit_far(seats: list[str], row: int, column: int):
    adj_seats = occupied_adjacent_seats_far(seats, row, column)
    seat = seats[row][column]
    if seat == 'L' and adj_seats == 0:
        return True
    elif seat == '#' and adj_seats < 5:
        return True
    else:
        return False


def occupied_adjacent_seats(seats: list[str], row: int, column: int):
    occupied_seats = 0
    occupied_seats += safe_seat_occupied(seats, row - 1, column - 1)
    occupied_seats += safe_seat_occupied(seats, row - 1, column)
    occupied_seats += safe_seat_occupied(seats, row - 1, column + 1)
    occupied_seats += safe_seat_occupied(seats, row, column - 1)
    occupied_seats += safe_seat_occupied(seats, row, column + 1)
    occupied_seats += safe_seat_occupied(seats, row + 1, column - 1)
    occupied_seats += safe_seat_occupied(seats, row + 1, column)
    occupied_seats += safe_seat_occupied(seats, row + 1, column + 1)
    return occupied_seats


def occupied_adjacent_seats_far(seats: list[str], row: int, column: int):
    occupied_seats = 0

    def seek_seat_in_direction(row_delta, column_delta):
        boat_rows = range(0, len(seats))
        boat_columns = range(0, len(seats[row]))
        found_occupied_chair = 0
        seek_row = row + row_delta
        seek_column = column + column_delta
        while not found_occupied_chair and seek_row in boat_rows and seek_column in boat_columns:
            seat = seats[seek_row][seek_column]
            if seat == '.':
                pass
            if seat == 'L':
                break
            if seat == '#':
                found_occupied_chair = 1
            seek_row += row_delta
            seek_column += column_delta
        return found_occupied_chair


    #1/8 directions
    occupied_seats += seek_seat_in_direction(-1, 0)   # N
    occupied_seats += seek_seat_in_direction(-1, 1)   # NE
    occupied_seats += seek_seat_in_direction(-1, -1)  # NW
    occupied_seats += seek_seat_in_direction(0, -1)   # W
    occupied_seats += seek_seat_in_direction(0, 1)    # E
    occupied_seats += seek_seat_in_direction(1, 0)    # S
    occupied_seats += seek_seat_in_direction(1, 1)    # SE
    occupied_seats += seek_seat_in_direction(1, -1)   # SW
    return occupied_seats


def safe_seat_is_chair(seats: list[str], row: int, column: int):
    try:
        if seats[row][column] == '.':
            return False
        else:
            return True
    except IndexError:
        return False


def safe_seat_occupied(seats: list[str], row: int, column: int):
    if row < 0 or column < 0:
        return False
    try:
        if seats[row][column] == '#':
            return 1
        else:
            return 0
    except IndexError:
        return 0


def compare_seats(seats1, seats2):
    difference = 0
    for row_index, row in enumerate(seats1):
        for seat_index, seat in enumerate(row):
            if seats2[row_index][seat_index] != seat:
                difference += 1
    return difference


def count_of_occupied_seats(seats: list[str]):
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1

    return count


def sit_passengers(seats: list[str]):
    seats_are_stable = False
    while not seats_are_stable:
        previous_seats = copy.deepcopy(seats)
        for row_index, row in enumerate(previous_seats):
            for seat_index, seat in enumerate(row):
                if seat != '.':
                    if seat_is_ok_to_sit(previous_seats, row_index, seat_index):
                        seats[row_index][seat_index] = '#'
                    else:
                        seats[row_index][seat_index] = 'L'
        difference = compare_seats(previous_seats, seats)
        if not difference:
            seats_are_stable = True
    return count_of_occupied_seats(seats)


def sit_passengers_far(seats: list[str]):
    seats_are_stable = False
    while not seats_are_stable:
        previous_seats = copy.deepcopy(seats)
        for row_index, row in enumerate(previous_seats):
            for seat_index, seat in enumerate(row):
                if seat != '.':
                    if seat_is_ok_to_sit_far(previous_seats, row_index, seat_index):
                        seats[row_index][seat_index] = '#'
                    else:
                        seats[row_index][seat_index] = 'L'
        difference = compare_seats(previous_seats, seats)
        if not difference:
            seats_are_stable = True
    return count_of_occupied_seats(seats)
