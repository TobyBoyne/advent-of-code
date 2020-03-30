from collections import Counter

def read_input():
	replacements = {}
	with open("day19.txt") as f:
		lines = f.readlines()
		for line in lines[:-2]:
			element, out_molecule = line.strip("\n").split(" => ")
			if element not in replacements:
				replacements[element] = []
			out_molecule_lst = molecule_to_list(out_molecule)
			replacements[element].append(out_molecule_lst)

		molecule = lines[-1].strip("\n")
	return molecule, replacements

def molecule_to_list(molecule):
	molecule_lst = []
	cur_molecule = ""
	for i, c in enumerate(molecule):
		cur_molecule += c
		if i < len(molecule) - 1 and molecule[i + 1].isupper():
			molecule_lst.append(cur_molecule)
			cur_molecule = ""

	molecule_lst.append(cur_molecule)
	return molecule_lst

def list_is_subset(lst, sub):
	for i in range(len(lst) - len(sub) + 1):
		if sub == lst[i:i+len(sub)]:
			return i
	return -1

def reduce(molecule_lst, origins, out_molecules, steps=0):
	for mol in out_molecules:
		idx = list_is_subset(molecule_lst, list(mol))
		if idx != -1:
			reduced_molecule_lst = molecule_lst[:idx] + [origins[mol]] + molecule_lst[idx + len(mol):]
			if reduced_molecule_lst in (['e'], ['H', 'F'], ['N', 'Al'], ['O', 'Mg']):
				print(steps, reduced_molecule_lst)
				return True
			else:
				r = reduce(reduced_molecule_lst, origins, out_molecules, steps+1)
				if r:
					print("Double Done!")

	return False


def part_one(molecule, replacements):
	molecule_lst = molecule_to_list(molecule)
	new_molecules = []
	for i, element in enumerate(molecule_lst):
		if element in replacements:
			for out_molecule in replacements[element]:
				new_molecule = molecule_lst[:i] + out_molecule + molecule_lst[i+1:]
				new_molecules.append(new_molecule)

	str_molecules = ["".join(m) for m in new_molecules]
	unique_molecules = set(str_molecules)
	return len(unique_molecules)

def part_two(molecule, replacements):
	molecule_lst = molecule_to_list(molecule)
	# origins dict stores ways that an output molecule can be made - reverse of replacements
	origins = {}
	for k, v in replacements.items():
		if k != 'e':
			for mol in v:
				origins[tuple(mol)] = k

	out_molecules = list(sorted(origins.keys(), key=lambda x: -len(x)))

	all_elements = [element for mol in out_molecules for element in mol]
	reduce(molecule_lst, origins, out_molecules)

molecule, replacements = read_input()
print(part_one(molecule, replacements))
print(part_two(molecule, replacements))