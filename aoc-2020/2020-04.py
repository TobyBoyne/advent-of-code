from string import hexdigits

with open('day04.txt') as f:
	passports = []
	for passport_str in f.read().split('\n\n'):
		passport_list = passport_str.replace('\n', ' ').split()
		passport = {}
		for sub in passport_list:
			k, v = sub.split(':')
			passport[k] = v

		passports.append(passport)

req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',)

def part_one():
	valid_count = 0
	for p in passports:
		valid_count += all(field in p for field in req_fields)

	return valid_count

def part_two():
	validation = {
		'byr': lambda x: x.isnumeric() and 1920 <= int(x) <= 2002,
		'iyr': lambda x: x.isnumeric() and 2010 <= int(x) <= 2020,
		'eyr': lambda x: x.isnumeric() and 2020 <= int(x) <= 2030,
		'hgt': lambda x: 'cm' in x and 150 <= int(x[:-2]) <= 193
		              or 'in' in x and 59 <= int(x[:-2]) <= 76,
		'hcl': lambda x: len(x) == 7 and x[0] == '#' and all(c in hexdigits for c in x[1:]),
		'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
		'pid': lambda x: len(x) == 9 and x.isnumeric(),
		'cid': lambda x: True
	}
	valid_count = 0
	for p in passports:
		for field in req_fields:
			if field not in p:
				break
			if not validation[field](p[field]):
				break

		else: #nobreak
			valid_count += 1

	return valid_count

print('Part one', part_one())
print('Part two', part_two())