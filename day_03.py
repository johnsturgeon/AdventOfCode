from math import prod


def tree_at_position(terrain, x, y):
    # X and Y are non-index based, so we need to shift -1
    y = y - 1
    x = x - 1
    # modulo x if it's beyond the right edge of the terrain
    x = x % len(terrain[y])
    if terrain[y][x] == '#':
        return True
    else:
        return False


def trees_hit(terrain, increment_x, increment_y):
    position = {"x": 1, "y": 1}
    # move to first position
    position['x'] += increment_x
    position['y'] += increment_y
    total_trees = 0
    for _ in terrain:
        if position['y'] > len(terrain):
            break
        if tree_at_position(terrain, position['x'], position['y']):
            total_trees += 1
        position['x'] += increment_x
        position['y'] += increment_y

    return total_trees


def product_trees_hit(terrain):
    return prod([
        trees_hit(terrain, increment_x=3, increment_y=1),
        trees_hit(terrain, increment_x=1, increment_y=1),
        trees_hit(terrain, increment_x=5, increment_y=1),
        trees_hit(terrain, increment_x=7, increment_y=1),
        trees_hit(terrain, increment_x=1, increment_y=2)
        ])
