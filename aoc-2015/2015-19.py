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

molecule, replacements = read_input()
print(part_one(molecule, replacements))