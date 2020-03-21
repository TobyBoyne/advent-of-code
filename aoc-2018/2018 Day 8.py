class Tree:
	def __init__(self):
		self.nodes = []
	def add(self, node):
		self.nodes.append(node)
	def ind(self, index):
		return self.nodes[index]

	def sum_of_nodes(self):
		return sum([node.sum_meta() for node in self.nodes])
	def value(self):
		return self.nodes[-1].value(self)

	def __repr__(self):
		return "\n".join(str(node) for node in self.nodes)

class Node:
	def __init__(self, index, children, metadata):
		self.i = index
		self.c = children
		self.meta = metadata
	def sum_meta(self):
		return sum(self.meta)
	def value(self, tree):
		if self.c:
			return sum([tree.ind(self.c[m - 1]).value(tree) for m in self.meta if m <= len(self.c)])
		else:
			return self.sum_meta()

	def __str__(self):
		return "["+str(self.i)+": "+str(self.c)+", "+str(self.meta)+"]"



def sum_metadata():
	with open("day8.txt", 'r') as f:
		numbers = [int(n) for n in f.read().strip("\n").split()]
	my_tree = Tree()
	index = 0
	current_data = ["header", -1, -1]

	# headers is a stack of lists
	# [num_children, num_metadata, num_children_already_added, children_indexes]
	headers = []

	i = 0
	complete = False
	while not complete:
		if current_data[0] == "header":
			headers.append(numbers[i : i + 2] + [0, []])

			if numbers[i] == 0:
				current_data = ["children"] + numbers[i : i + 2]
			i += 2
		elif current_data[0] == "children":
			current_data[0] = "metadata"

		elif current_data[0] == "metadata":
			metadata = numbers[i : i + current_data[2]]
			i += current_data[2]
			if len(headers) > 1:
				headers[-2][3].append(index)
			children = headers[-1][3]

			my_tree.add(Node(index, children, metadata))

			index += 1
			headers.pop()
			if headers:
				headers[-1][2] += 1

			# if headers is empty, then all nodes have been read
			if headers:
				# if the number of children already added is equal to the number of children for that node
				if headers[-1][2] == headers[-1][0]:
					current_data = ["children"] + headers[-1][:2]
				else:
					current_data = ["header", -1, -1]
			else:
				complete = True



	print(my_tree)
	print(my_tree.sum_of_nodes())
	print(my_tree.value())

sum_metadata()