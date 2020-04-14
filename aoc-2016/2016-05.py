from hashlib import md5


def part_one(string):
	password = ''
	for i in range(10253167):
		hashed_string = md5((string + str(i)).encode()).hexdigest()
		if hashed_string[:5] == '00000':
			password += hashed_string[5]
			if len(password) == 8:
				return password
	return "Failed"

def part_two(string):
	password = ['' for _ in range(8)]
	for i in range(25176242):
		hashed_string = md5((string + str(i)).encode()).hexdigest()
		if hashed_string[:5] == '00000':
			pos = hashed_string[5]
			if '0' <= pos <= '7' and not password[int(pos)]:
				password[int(pos)] = hashed_string[6]
				if all(password):
					return ''.join(password)


puzz_input = "ugkcyxxp"
print(part_one(puzz_input))
print(part_two(puzz_input))