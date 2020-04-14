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




puzz_input = "ugkcyxxp"
print(part_one(puzz_input))
