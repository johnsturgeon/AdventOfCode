import re


def validate_byr(byr: str):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002


def validate_iyr(iyr: str):
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020


def validate_eyr(eyr: str):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030


def validate_hgt(hgt: str):
    m = re.match(r"(\d+)(.*)", hgt)
    height = int(m.groups()[0])
    unit = m.groups()[1]
    if unit == 'cm':
        return 150 <= height <= 193
    elif unit == 'in':
        return 59 <= height <= 76
    else:
        return False


def validate_hcl(hcl: str):
    return re.search(r"^#[0-9a-f]{6}$", hcl)


def validate_ecl(ecl: str):
    valid_ecl = False
    for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        if ecl == color:
            valid_ecl = True
            break
    return valid_ecl


def validate_pid(pid: str):
    return re.search(r"^[0-9]{9}$", pid)


def mandatory_elements():
    return {'byr': validate_byr,
            'iyr': validate_iyr,
            'eyr': validate_eyr,
            'hgt': validate_hgt,
            'hcl': validate_hcl,
            'ecl': validate_ecl,
            'pid': validate_pid
            }


def validate_fields(passport_data: str):
    fields = passport_data.split()
    element_validator = mandatory_elements()
    ecl_count = 0
    for field in fields:
        key, value = field.split(':')
        if key == 'ecl':
            ecl_count += 1
        if key in element_validator and not element_validator[key](value):
            return False
    assert ecl_count == 1
    return True


def valid_passports(passport_data: list, should_validate_fields=False):
    elements_dict = mandatory_elements()
    element_keys = list(elements_dict.keys())

    valid_passport_count = 0
    passport_string = ""
    for line in passport_data:
        if line:
            passport_string += " " + line
        else:
            is_valid = True
            for element in element_keys:
                if element not in passport_string:
                    is_valid = False
                    break
            if is_valid:
                if not should_validate_fields:
                    valid_passport_count += 1
                elif validate_fields(passport_string):
                    valid_passport_count += 1
            passport_string = ""

    return valid_passport_count
