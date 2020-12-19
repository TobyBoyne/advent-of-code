with open('day05.txt') as f:
	seats = [''.join('1' if c in 'BR' else '0' for c in l.rstrip()) for l in f.readlines()]

def part_one():
	return max(int(seat, 2) for seat in seats)

def part_two():
	seat_ids = {int(seat, 2) for seat in seats}
	for i in range(89, 989):
		if i not in seat_ids: return i

print('Part one', part_one())
print('Part two', part_two())