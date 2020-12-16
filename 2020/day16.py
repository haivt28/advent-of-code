input = open('input/day16.txt').read()


field_to_range = {}
all_valid_range = set()

verified = {}
my_ticket = []

error_rate = 0
departure_result = 1

for line in input.split('\n'):
    if 'or' in line:
        field = line.split(':')[0]
        range1, _, range2 = line.split(':')[1].strip().split()
        range1 = list(range(int(range1.split('-')[0]), int(range1.split('-')[1]) + 1))
        range2 = list(range(int(range2.split('-')[0]), int(range2.split('-')[1]) + 1))

        field_to_range[field] = set(range1 + range2)
        all_valid_range.update(range1)
        all_valid_range.update(range2)

    elif 'ticket' not in line and line != '':
        fields = list(map(int, line.split(',')))
        for field in fields:
            if field not in all_valid_range:
                error_rate += field
            else:
                if len(my_ticket) < len(fields):
                    my_ticket.append(field)

                valid_fields = set([k for k, v in field_to_range.items() if field in v])

                index = fields.index(field)
                if index not in verified:
                    verified[index] = valid_fields
                else:
                    verified[index] = verified[index] & valid_fields  # intersection

all_fields = []
for k in sorted(verified, key=lambda k: len(verified[k])):
    remain_field = [item for item in verified[k] if item not in all_fields]
    all_fields.extend(remain_field)
    if remain_field[0].startswith('departure'):
        departure_result *= my_ticket[k]

# PART 1
print(error_rate)

# PART 2
print(departure_result)
