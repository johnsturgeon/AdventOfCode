
def get_seat_id(tickets, get_my_seat=False):
    all_seats = []
    max_row_id = 0
    for ticket in tickets:
        rows = list(range(0, 128))
        columns = list(range(0, 8))
        for i in range(0, 7):
            if ticket[i] == 'B':
                rows = rows[len(rows)//2:]
            else:
                rows = rows[:len(rows)//2]
        for i in range(7, 10):
            if ticket[i] == 'R':
                columns = columns[len(columns)//2:]
            else:
                columns = columns[:len(columns)//2]
        assert len(rows) == 1
        assert len(columns) == 1
        row_id = rows[0] * 8 + columns[0]
        all_seats.append(row_id)
        max_row_id = max(row_id, max_row_id)

    if get_my_seat:
        sorted_seats = sorted(all_seats)
        next_seat_index = 1
        for seat in sorted_seats:
            if seat + 1 != sorted_seats[next_seat_index]:
                return seat + 1
            else:
                next_seat_index += 1
    else:
        return max_row_id
