from hashlib import md5

string = "ckczppom"

for i in range(100000000):
	hashed_string = md5((string + str(i)).encode()).hexdigest()
	if hashed_string[:5] == '00000':
		print("Part one", i)
	if hashed_string[:6] == '000000':
		print("Part two", i)
		break