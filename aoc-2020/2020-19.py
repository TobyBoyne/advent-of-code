from parse import parse
from itertools import product, chain

with open('day19.txt') as f:
	reading_rules =True
	rules = {}
	rules_as_str = {}
	msgs = []
	for l in f.readlines():
		line = l.rstrip()
		if not line:
			reading_rules = False
		elif reading_rules:
			rule_no, r = parse('{:d}: {}', line).fixed
			if '"' in r:
				rules_as_str[rule_no] = [r.strip('"')]
			else:
				rule = r.split(' | ')
				rules[rule_no] = [[int(x) for x in sub_rule.split()] for sub_rule in rule]

		else:
			msgs.append(line)


def valid_combs(n):
	if n in rules_as_str:
		return rules_as_str[n]
	sub_rules = rules[n]
	combs = []
	for sub in sub_rules:
		prod = list(product(*(valid_combs(r) for r in sub)))
		combs += prod

	combs_as_str = [''.join(s) for s in combs]
	rules_as_str[n] = combs_as_str
	return combs_as_str


all_valid_messages = set(valid_combs(0))

def part_one():
	return sum(m in all_valid_messages for m in msgs)

print('Part one', part_one())
