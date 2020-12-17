def get_waypoint_directions(relative_directions):
    headings = ['N', 'E', 'S', 'W']
    waypoint = {0: 1, 1: 10}
    current_heading_index = 1
    absolute_directions = []
    for direction in relative_directions:
        heading = direction[:1]
        distance = int(direction[1:])
        if heading in headings:
            heading_index = headings.index(heading)
            opposite_heading = (heading_index + 2) % 4
            if heading_index in waypoint:
                waypoint[heading_index] += distance
            else:
                opposite_distance = waypoint[opposite_heading]
                new_distance = opposite_distance - distance
                if new_distance < 0:
                    new_distance = new_distance * -1
                    waypoint.pop(opposite_heading)
                    waypoint[heading_index] = new_distance
                else:
                    waypoint[opposite_heading] = new_distance
        if heading == 'F':
            for point in waypoint:
                head = headings[point]
                amt = waypoint[point]
                absolute_directions.append(head + str(amt * distance))
        if heading == 'R':
            new_waypoint = {}
            for wp_heading in waypoint:
                new_heading = wp_heading
                new_heading += int((int(distance) / 90))
                new_heading = new_heading % len(headings)
                new_waypoint[new_heading] = waypoint[wp_heading]
            waypoint = new_waypoint
        if heading == 'L':
            new_waypoint = {}
            for wp_heading in waypoint:
                new_heading = wp_heading
                new_heading -= int((int(distance) / 90))
                new_heading = new_heading % len(headings)
                new_waypoint[new_heading] = waypoint[wp_heading]
            waypoint = new_waypoint

    return absolute_directions


def get_absolute_directions(relative_directions):
    headings = ['N', 'E', 'S', 'W']
    current_heading_index = 1
    absolute_directions = []
    for direction in relative_directions:
        heading = direction[:1]
        distance = direction[1:]
        if heading in headings:
            absolute_directions.append(direction)
        if heading == 'F':
            heading = headings[current_heading_index]
            absolute_directions.append(heading + distance)
        if heading == 'R':
            current_heading_index += int((int(distance) / 90))
            current_heading_index = current_heading_index % len(headings)
        if heading == 'L':
            current_heading_index -= int((int(distance) / 90))
            current_heading_index = current_heading_index % len(headings)

    return absolute_directions


def get_manhattan_distance(relative_directions, use_waypoint=False):
    if use_waypoint:
        absolute_directions = get_waypoint_directions(relative_directions)
    else:
        absolute_directions = get_absolute_directions(relative_directions)
    total_distances = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    for direction in absolute_directions:
        heading = direction[:1]
        distance = direction[1:]
        total_distances[heading] += int(distance)

    return abs(total_distances['N'] - total_distances['S']) + abs(total_distances['E'] - total_distances['W'])
