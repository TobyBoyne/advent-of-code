from parse import parse

compounds = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1
}

def read_input():
	def grouper(it):
		# collect details as (key, value) pairs
		args = [iter(it)] * 2
		return zip(*args)

	with open("day16.txt") as f:
		lines = f.readlines()
		sue_details = []
		for line in lines:
			p = parse("Sue {}: {}: {:d}, {}: {:d}, {}: {:d}",
					  line.strip("\n"))
			_, *details = p.fixed
			detail_dict = {detail: value for detail, value in grouper(details)}
			sue_details.append(detail_dict)
		return sue_details


def part_one(sue_details):
	for i, details in enumerate(sue_details):
		if all(compounds[d] == v for d, v in details.items()):
			return i + 1

	return -1

def part_two(sue_details):
	for i, details in enumerate(sue_details):
		real_sue = True
		for d, v in details.items():
			if d in ("cats", "trees"):
				if v <= compounds[d]:
					real_sue = False
			elif d in ("pomeranians", "goldfish"):
				if v >= compounds[d]:
					real_sue = False
			elif v != compounds[d]:
				real_sue = False
		if real_sue:
			return i + 1

	return -1


sue_details = read_input()
print(part_one(sue_details))
print(part_two(sue_details))