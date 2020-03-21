class Scanner:
	def __init__(self, depth, r):
		self.depth = depth
		self.r = r
	def intersects(self, delay=0):
		return (self.depth + delay) % (2 * self.r - 2) == 0
	def score(self, delay=0):
		return self.intersects(delay) * self.depth * self.r


def read_file():
	scanners = {}
	with open("day13.txt", 'r') as f:
		for line in f:
			depth, r = [int(v) for v in line.strip("\n").split(": ")]
			scanners[depth] = Scanner(depth, r)
	return scanners

def run(scanners):
	score = 0
	for s in scanners:
		score += scanners[s].score()
	return score

def min_delay(scanners):
	delay = 0
	while any([scanners[s].intersects(delay) for s in scanners]):
		delay += 1
		if delay % 100000 == 0: print(delay)
	return delay

scanners = read_file()

print("Part one:", run(scanners))
print("Part two:", min_delay(scanners))