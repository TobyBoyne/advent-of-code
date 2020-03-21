import hashlib as hl

DOOR_ID = "ugkcyxxp"
DOOR_ID = "abc"

def find_password(door):
	h = hl.new('md5')
	i = 0
	password = ""
	while True:
		h.update((door + str(i)).encode("UTF-8"))
		hashed_word = h.hexdigest()
		if hashed_word[:5] == "00000":
			print(hashed_word)
			print(i)
		i += 1


print(find_password(DOOR_ID))