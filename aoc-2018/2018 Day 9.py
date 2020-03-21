# 448 players; last marble is worth 71628 points
import time


class Marble:
	def __init__(self):
		self.v = 0
		self.child = -1
		self.parent = -1


class Circle:
	def __init__(self, num_players, last_marble):
		self.num_players = num_players
		self.last_marble = last_marble
		self.c_length = 1
		self.current_marble = 0
		self.player_scores = {i : 0 for i in range(num_players)}
		self.player = 0

		self.marbles = [Marble() for i in range(last_marble)]
		self.marbles[0].child = 0
		self.free = 1

	def anti_clock(self, index, n):
		if n == 0:
			return index
		else:
			return self.anti_clock(self.marbles[index].parent, n - 1)

	def play_game(self):
		for marble in range(1, self.last_marble + 1):
			self.play_marble(marble)
			self.player = (self.player+1) % self.num_players
		return self.player_scores[max(self.player_scores, key=self.player_scores.get)]

	def play_marble(self, value):
		if value % 23:
			add_index = self.marbles[self.current_marble].child
			self.marbles[self.free].v = value
			self.marbles[self.free].child = self.marbles[add_index].child
			self.marbles[self.free].parent = add_index
			self.marbles[self.marbles[add_index].child].parent = self.free
			self.marbles[add_index].child = self.free

			self.current_marble = self.free
			self.free += 1
		else:
			self.del_marble(value)


	def del_marble(self, value):
		del_index = self.anti_clock(self.current_marble, 7)
		parent_index = self.marbles[del_index].parent
		child_index = self.marbles[del_index].child
		self.marbles[parent_index].child = child_index
		self.marbles[child_index].parent = parent_index

		self.current_marble = child_index
		self.player_scores[self.player] += value + self.marbles[del_index].v

	def __repr__(self):
		i = 0
		output = []
		while not output or i != 0:
			if i == self.current_marble:
				output.append("(" + str(self.marbles[i].v) + ")")
			else:
				output.append(self.marbles[i].v)
			i = self.marbles[i].child
		return str(output)

t = time.perf_counter()

my_game = Circle(448, 7162800)
print("Time to initialise:", time.perf_counter() - t)
print(my_game.play_game())
print("Time to complete:", time.perf_counter() - t)