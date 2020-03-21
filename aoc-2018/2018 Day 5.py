"""
OLD Method - had memory issues
def length_after_reaction(polymer):
	reaction_flag = True

	while reaction_flag:
		reaction_flag = False
		i = 0
		while i < len(polymer) - 1:
			if abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32:
				polymer = polymer[:i] + polymer[i + 2:]
				i -= 2
				reaction_flag = True
			i += 1

	print(len(polymer))
"""

P = open("day5.txt", 'r').read()

class Tree:
	class Node:
		def __init__(self, parent, pointer):
			self.parent = parent
			self.pointer = pointer
	def __init__(self, polymer):
		self.polymer = polymer
		self.nodes = [Tree.Node(i - 1, i + 1) for i in range(len(polymer) - 1)]
		self.nodes.append(Tree.Node(len(polymer) - 2, -1))
		self.head_pointer = 0

	def remove_node_pair(self, index):
		parent_pointer = self.nodes[index].parent
		child_pointer = self.nodes[self.nodes[index].pointer].pointer
		if parent_pointer != -1 and child_pointer != -1:
			self.nodes[parent_pointer].pointer = child_pointer
			self.nodes[child_pointer].parent = parent_pointer
		elif parent_pointer == -1:
			self.nodes[child_pointer].parent = -1
			self.head_pointer = child_pointer
		elif child_pointer == -1:
			self.nodes[parent_pointer].pointer = -1

	def react(self):
		reaction_flag = True
		while reaction_flag:
			reaction_flag = False
			index = self.head_pointer
			while self.nodes[index].pointer != -1:
				if abs(ord(self.polymer[index]) - ord(self.polymer[self.nodes[index].pointer])) == 32:
					temp_index = index
					index = self.nodes[index].parent
					self.remove_node_pair(temp_index)
					reaction_flag = True
				else:
					index = self.nodes[index].pointer

	def polymer_length(self):
		length = 1
		index = self.head_pointer
		final_polymer = ""
		while self.nodes[index].pointer != -1:
			length += 1
			final_polymer+=self.polymer[index]
			index = self.nodes[index].pointer


		final_polymer+=self.polymer[index]
		return length


def remove_one_unit(polymer):
	for letter in map(chr, range(97, 123)):
		new_polymer = polymer.replace(letter, '').replace(letter.upper(), '')
		removed_P_tree = Tree(new_polymer)
		removed_P_tree.react()
		print("Letter removed:", letter, "New length:", removed_P_tree.polymer_length())


P_tree = Tree(P)
P_tree.react()
print(P_tree.polymer_length())

remove_one_unit(P)