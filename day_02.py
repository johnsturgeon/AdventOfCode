def parse_password(password_line: str):
    # parse the line ("1-3 a: abcde")
    tokens = password_line.split()
    a_list = tokens[0].split('-')
    first_number, second_number = map(int, a_list)
    char_to_check = tokens[1].strip(':')
    password = tokens[2]
    return {
        "first_number": first_number,
        "second_number": second_number,
        "char_to_check": char_to_check,
        "password": password
    }


def valid_password_by_occurance(password_line: str):
    parsed_password = parse_password(password_line)
    count = 0
    for c in parsed_password['password']:
        if parsed_password['char_to_check'] == c:
            count += 1
    if parsed_password['first_number'] <= count <= parsed_password['second_number']:
        return True
    else:
        return False


def valid_password_by_position(password_line: str):
    parsed_password = parse_password(password_line)
    count = 0
    if parsed_password['password'][parsed_password['first_number']-1] == parsed_password['char_to_check']:
        count += 1
    if parsed_password['password'][parsed_password['second_number']-1] == parsed_password['char_to_check']:
        count += 1
    if count == 1:
        return True
    else:
        return False


def count_valid_passwords_by_occurrence(password_list):
    valid_password_count = 0
    for line in password_list:
        if valid_password_by_occurance(line):
            valid_password_count += 1
    return valid_password_count


def count_valid_passwords_by_position(password_list):
    valid_password_count = 0
    for line in password_list:
        if valid_password_by_position(line):
            valid_password_count += 1
    return valid_password_count
