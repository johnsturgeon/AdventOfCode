def get_sum_of_answers(list_of_answers):
    customs_answers = ""
    sum_of_answers = 0
    for line in list_of_answers:
        if line and line != 'EOF':
            customs_answers += line
        else:
            sum_of_answers += len(set(customs_answers))
            customs_answers = ""
    return sum_of_answers


def get_intersection_of_answers(list_of_answers):
    intersection_of_answers = None
    sum_of_answers = 0
    for line in list_of_answers:
        if line and line != 'EOF':
            if intersection_of_answers is None:
                intersection_of_answers = set(line)
            else:
                intersection_of_answers = intersection_of_answers.intersection(set(line))
        else:
            sum_of_answers += len(set(intersection_of_answers))
            intersection_of_answers = None
    return sum_of_answers
