from itertools import combinations

class Character:
	def __init__(self, hp, dmg, armour):
		self.hp = hp
		self.dmg = dmg
		self.armour = armour
	def damage_per_turn(self, other):
		return max(self.dmg - other.armour, 1)
	def turns_to_beat(self, other):
		return other.hp // self.damage_per_turn(other)

class Item:
	def __init__(self, cost=0, dmg_bonus=0, armour_bonus=0):
		self.cost = cost
		self.dmg_bonus = dmg_bonus
		self.armour_bonus = armour_bonus
	def __add__(self, other):
		return Item(self.cost+other.cost, self.dmg_bonus+other.dmg_bonus, self.armour_bonus+other.armour_bonus)

def armour_needed_given_dmg(boss, player, dmg):
	for i in range(10):
		test_player = Character(player.hp, dmg, i)
		if test_player.turns_to_beat(boss) <= boss.turns_to_beat(test_player):
			return i
	return -1

def all_combinations(weapons, armours, rings):
	combs = {}
	for w in weapons:
		for a in armours:
			for (r1, r2) in combinations(rings, r=2):
				total_item = sum((w, a, r1, r2), Item())
				dmg, armour, cost = total_item.dmg_bonus, total_item.armour_bonus, total_item.cost
				if (dmg, armour) in combs:
					cost = min(combs[(dmg, armour)], cost)
				combs[(dmg, armour)] = cost
	return combs


def part_one(boss, player, all_combs):
	dmg_armour_dict = {}
	for dmg in range(4, 14):
		armour = armour_needed_given_dmg(boss, player, dmg)
		if armour not in dmg_armour_dict.values():
			dmg_armour_dict[dmg] = armour

	min_cost = 1000
	for stats in dmg_armour_dict.items():
		min_cost = min(min_cost, all_combs[(stats)])

	return min_cost



boss = Character(hp=100, dmg=8, armour=2)
player = Character(hp=100, dmg=0, armour=0)

# armour and rings are optional - include choice of taking a blank item
weapons = [Item(8, 4, 0), Item(10, 5, 0), Item(25, 6, 0), Item(40, 7, 0), Item(74, 8, 0)]
armours = [Item(13, 0, 1), Item(31, 0, 2), Item(53, 0, 3), Item(75, 0, 4), Item(102, 0, 5), Item()]
rings = [Item(25, 1, 0), Item(50, 2, 0), Item(100, 3, 0), Item(20, 0, 1), Item(40, 0, 2), Item(80, 0, 3), Item(), Item()]
all_items = (weapons, armours, rings)
all_combs = all_combinations(*all_items)
print(part_one(boss, player, all_combs))