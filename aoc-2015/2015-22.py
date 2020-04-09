
# TODO: rethink brute force; stop repeats of effects before effect has ended

class Character:
	def __init__(self, hp, dmg=0, armour=0):
		self.hp = hp
		self.dmg = dmg
		self.armour = armour

	def damage(self, other):
		other.hp -= max(self.dmg - other.armour, 1)

	@property
	def is_dead(self):
		return self.hp <= 0 or (self.__class__ == Wizard and self.mana <= 0)

	def copy(self):
		return Character(self.hp, self.dmg, self.armour)
	def __repr__(self):
		return f"{self.__class__.__name__}(hp={self.hp})"

class Wizard(Character):
	def __init__(self, hp, dmg=0, armour=0, mana=0):
		super().__init__(hp, dmg, armour)
		self.mana = mana
		all_effects = (effect for _, (_, effect) in Wizard.spells.items() if effect)
		self.effects = {effect: [None, 0] for effect in all_effects}

		self.mana_spent = 0
		self.spell_history = []

	def new_turn(self, other):
		self.armour = 0
		for name, (effect, duration) in self.effects.items():
			if duration > 0:
				effect(self, other)
				self.effects[name][1] -= 1

	def available_spells(self):
		# returns all regular spells, as well as effect spells that can be cast
		available = []
		for spell, (_, spell_effect) in Wizard.spells.items():
			if not spell_effect or self.effects[spell_effect][1] == 0:
				available.append(spell)
		return available

	def cast_spell(self, spell, target):
		spell(self, target)
		cost = Wizard.spells[spell][0]
		self.mana_spent += cost
		self.spell_history = self.spell_history + [spell.__name__]

	def magic_missile(self, other):
		other.hp -= 4

	def drain(self, other):
		other.hp -= 2
		self.hp += 2

	def shield(self, other=None):
		def shield_effect(player, other):
			player.armour = 7
		self.effects['shield_effect'] = [shield_effect, 6]

	def poison(self, other):
		def poison_effect(player, other):
			other.hp -= 3
		self.effects['poison_effect'] = [poison_effect, 6]

	def recharge(self, other=None):
		def recharge_effect(player, other):
			player.mana += 101
		self.effects['recharge_effect'] = [recharge_effect, 5]


	def copy(self):
		new_wizard = Wizard(self.hp, mana=self.mana)
		new_wizard.effects = {name: [effect, dur] for name, (effect, dur) in self.effects.items()}
		new_wizard.mana_spent = self.mana_spent
		new_wizard.spell_history = self.spell_history
		return new_wizard


	spells = {
		magic_missile: (53, None),
		drain: (73, None),
		shield: (113, 'shield_effect'),
		poison: (173, 'poison_effect'),
		recharge: (229, 'recharge_effect')
	}


def gen_new_battles(player: Wizard, boss: Character):
	new_battles = []
	for spell in player.available_spells():
		new_player = player.copy()
		new_boss = boss.copy()
		new_player.cast_spell(spell, new_boss)
		new_battles.append((new_player, new_boss))
	return new_battles



def part_one(player: Wizard, boss: Character):
	# simulate battles for all combinations of spells cast
	new_battles = gen_new_battles(player, boss)
	print(new_battles)
	cheapest_win = 10000
	while new_battles:
		#print(new_battles)
		cur_battles = new_battles
		new_battles = []
		for p, b in cur_battles:
			# start new turn (so that poison might defeat boss)
			# if the boss is dead, stop the battle and check total mana spent
			# else, deal his damage and generate next choices of spells
			p.new_turn(b)

			if b.is_dead:
				if (total_mana := p.mana_spent) < cheapest_win:
					cheapest_win = total_mana
					print(p, b, p.mana_spent, p.spell_history)
			else:
				b.damage(p)
				if not p.is_dead:
					p.new_turn(b)
					new_battles += gen_new_battles(p, b)

	return cheapest_win




boss = Character(hp=58, dmg=9)
player = Wizard(hp=50, mana=500)
# print(player.available_spells())
# player.cast_spell(Wizard.poison, boss)
# print(player.effects)
# player.new_turn()
# print(player.effects)
# print(player.available_spells())
print(part_one(player, boss))