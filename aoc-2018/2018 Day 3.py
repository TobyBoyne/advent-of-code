# count across then down (scan)

def count_clashes():
	grid = {i:0 for i in range(10**6)}
	with open("day3.txt", "r") as f:
		for line in f:
			*_, corner, size = line.strip("\n").split()
			top_x, top_y = [int(X) for X in corner.strip(":").split(",")]
			size_x, size_y = [int(X) for X in size.split("x")]
			for x in range(top_x, top_x + size_x):
				for y in range(top_y, top_y + size_y):
					grid[1000*y + x] += 1
	return	sum([grid[key] > 1 for key in grid])

def intact_claim():
	grid={i:0 for i in range(10**6)}
	with open("day3.txt","r") as f:
		for line in f:
			*_, corner, size=line.strip("\n").split()
			top_x,top_y=[int(X) for X in corner.strip(":").split(",")]
			size_x,size_y=[int(X) for X in size.split("x")]
			for x in range(top_x,top_x+size_x):
				for y in range(top_y,top_y+size_y):
					grid[1000*y+x]+=1
		f.seek(0)
		for line in f:
			no_clash = True
			claim_id, _, corner, size = line.strip("\n").split()
			top_x,top_y=[int(X) for X in corner.strip(":").split(",")]
			size_x,size_y=[int(X) for X in size.split("x")]
			for x in range(top_x,top_x+size_x):
				for y in range(top_y,top_y+size_y):
					if grid[1000*y+x] > 1:
						no_clash = False

			if no_clash:
				return claim_id

print(intact_claim())