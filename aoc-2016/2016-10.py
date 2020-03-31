from parse import parse
from collections import defaultdict
from copy import deepcopy

def read_input():
	with open("day10.txt") as f:
		bots_values = defaultdict(list)
		comparisons = {}
		for line in f:
			if "value" in line:
				p = parse("value {:d} goes to bot {:d}", line.strip("\n"))
				value, bot = p.fixed
				bots_values[bot].append(value)
			else:
				p = parse("bot {:d} gives low to {} {:d} and high to {} {:d}", line.strip("\n"))
				bot, low_1, low_2, high_1, high_2 = p.fixed
				comparisons[bot] = ((low_1, low_2), (high_1, high_2))

	return bots_values, comparisons

def run_bots(bots, comparisons, stop_at=None):
	outputs = {}
	next_bots = {b for b in bots if len(bots[b]) == 2}

	while next_bots:
		cur_bots = {b for b in next_bots if len(bots[b]) == 2}
		next_bots = set()
		for bot in cur_bots:
			bot_values = sorted(bots[bot])
			for i, (is_bot, num) in enumerate(comparisons[bot]):
				# i==0 for low, i==1 for high
				v = bot_values[i]
				if is_bot == 'bot':
					bots[num].append(v)
					if stop_at and set(bots[num]) == stop_at:
						return num
					next_bots.add(num)
				else:
					outputs[num] = v
			bots[bot] = []

	return bots, outputs


def part_one(bots, comparisons):
	# deepcopy means that values are not copied between parts one and two
	bot_with_target_pair = run_bots(deepcopy(bots), comparisons, stop_at={61, 17})
	return bot_with_target_pair

def part_two(bots, comparisons):
	_, outputs = run_bots(deepcopy(bots), comparisons)
	return outputs[0] * outputs[1] * outputs[2]

instructions = read_input()
print(part_one(*instructions))
print(part_two(*instructions))