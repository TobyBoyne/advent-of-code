from collections import Counter
from string import ascii_lowercase as letters


def remove_decoys(rooms):
	sector_sum = 0
	real_rooms = []
	for room in rooms:
		name, sector_id, checksum = room
		count = Counter(name.replace("-", ""))
		ordered_count = sorted(count.most_common(), key=lambda x: (-x[1], x[0]))
		top_five = list(zip(*ordered_count))[0][:5]
		if "".join(map(str, top_five)) == checksum:
			sector_sum += int(sector_id)
			real_rooms.append(room)

	print("PART ONE:", sector_sum)
	return real_rooms


def find_room(rooms, search="northpole object storage"):
	real_rooms = remove_decoys(rooms)
	for name, sector_id, _ in real_rooms:
		words = name.split("-")
		decrypted = [[letters[(ord(c) - ord("a") + int(sector_id)) % 26] for c in word] for word in words]
		real_name = " ".join("".join(word) for word in decrypted)
		if real_name == search:
			print("PART TWO:", sector_id)
			break


with open("day4.txt", "r") as f:
	rooms = [(line[:-11], line[-10:-7], line[-6:-1]) for line in map(lambda s: s.strip("\n"), f)]

find_room(rooms)
