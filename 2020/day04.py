import re


input = open('input/day04.txt').read()


def check_valid_passport(passport):
    if 'byr' not in passport or 1920 > int(passport['byr']) or int(passport['byr']) > 2002:
        return False

    if 'iyr' not in passport or 2010 > int(passport['iyr']) or int(passport['iyr']) > 2020:
        return False

    if 'eyr' not in passport or 2020 > int(passport['eyr']) or int(passport['eyr']) > 2030:
        return False

    if 'hgt' in passport:
        if passport['hgt'].endswith('cm'):
            hgt = int(passport['hgt'].replace('cm', '').strip())
            if 150 > hgt or hgt > 193:
                return False
        else:
            hgt = int(passport['hgt'].replace('in', '').strip())
            if 59 > hgt or hgt > 76:
                return False
    else:
        return False

    if 'hcl' not in passport or not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False

    if 'ecl' not in passport or passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if 'pid' not in passport or not re.match(r'^[0-9]{9}$', passport['pid']):
        return False

    return True


# PART 1
passport_data = {}
valid_count = 0
for line in (input+'\n').split('\n'):
    if line == '':
        if len(passport_data.keys()) == 8 or (len(passport_data.keys()) == 7 and 'cid' not in passport_data):
            valid_count += 1
        passport_data = {}
    for data in line.split():
        # print(data)
        passport_data[data.split(':')[0]] = data.split(':')[1]

print(valid_count)


# PART 2
passport_data = {}
valid_count = 0
for line in (input+'\n').split('\n'):
    if line == '':
        if check_valid_passport(passport_data):
            valid_count += 1
        passport_data = {}
    for data in line.split():
        # print(data)
        passport_data[data.split(':')[0]] = data.split(':')[1]

print(valid_count)
