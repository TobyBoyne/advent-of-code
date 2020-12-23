from parse import parse
import numpy as np

with open('day16.txt') as f:
	section = 'fields'
	fields = {}
	my_ticket = []
	tickets = []
	for line in f.readlines():
		l = line.rstrip()
		if section == 'fields':
			if not l:
				section = 'your ticket'
			else:
				field, r1, r2, r3, r4 = parse('{}: {:d}-{:d} or {:d}-{:d}', l)
				fields[field] = [(r1, r2), (r3, r4)]

		elif section == 'your ticket':
			if not l:
				section = 'nearby tickets'
			elif 'your ticket' not in l:
				my_ticket = [int(v) for v in l.split(',')]

		elif section == 'nearby tickets':
			if 'nearby tickets' not in l:
				tickets.append([int(v) for v in l.split(',')])



def part_one():
	valid_values = np.zeros(1000)
	for field_ranges in fields.values():
		for r in field_ranges:
			valid_values[r[0] : r[1]+1] = 1

	error_rate = 0
	valid_tickets = []
	for ticket in tickets:
		valid= True
		for v in ticket:
			if not valid_values[v]:
				error_rate += v
				valid = False

		if valid:
			valid_tickets.append(ticket)

	return error_rate, valid_tickets


def within_ranges(r, value):
	return r[0][0] <= value <= r[0][1] or r[1][0] <= value <= r[1][1]

error_rate, valid_tickets = part_one()

def part_two():
	valid_field_idxs = {field: [1 for _ in range(len(fields))] for field in fields}
	for ticket in valid_tickets:
		for field, r in fields.items():
			for idx, value in enumerate(ticket):
				if not within_ranges(r, value):
					valid_field_idxs[field][idx] = 0

	# eliminate possibilities
	confirmed_field_idxs = {field: -1 for field in fields}
	field_order = list(sorted(valid_field_idxs.items(), key=lambda x: sum(x[1])))
	for field, idxs in field_order:
		idxs_remaining = [0 if i in confirmed_field_idxs.values() else v for i, v in enumerate(idxs)]
		confirmed_field_idxs[field] = idxs_remaining.index(1)

	departure_values = [my_ticket[idxs] for field, idxs in confirmed_field_idxs.items() if 'departure' in field]
	prod = 1
	for d in departure_values:
		prod *= d
	return prod

print('Part one', error_rate)
print('Part two', part_two())