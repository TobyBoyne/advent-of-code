from parse import parse
from collections import defaultdict

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


def part_one(bots, comparisons):
	outputs = {}
	next_bots = {b for b in bots if len(bots[b]) == 2}

	while ([17, 61] not in bots.values()) and ([61, 17] not in bots.values()):
		cur_bots = {b for b in next_bots if len(bots[b]) == 2}
		next_bots = set()
		for bot in cur_bots:
			bot_values = sorted(bots[bot])
			for i, (is_bot, num) in enumerate(comparisons[bot]):
				# i==0 for low, i==1 for high
				v = bot_values[i]
				if is_bot == 'bot':
					bots[num].append(v)
					next_bots.add(num)
				else:
					outputs[num] = v
			bots[bot] = []

	bot_with_target_pair = [b for b, v in bots.items() if {17, 61}.issubset(v)][0]
	return bot_with_target_pair

instructions = read_input()
print(part_one(*instructions))