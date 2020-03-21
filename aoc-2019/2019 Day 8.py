import matplotlib.pyplot as plt
import numpy as np

# x = np.array([[0, 1], [1, 0]])
# plt.imshow(x)
# plt.show()

SIZE = (6, 25)

def read_file():
	with open("day8.txt") as f:
		return f.read().strip("\n")


def part_one(digits):
	layer_size = SIZE[0] * SIZE[1]
	layers = [digits[i : i + layer_size] for i in range(0, len(digits), layer_size)]
	fewest_zeros = min(layers, key=lambda l: l.count('0'))
	checksum = fewest_zeros.count('1') * fewest_zeros.count('2')
	return checksum


def top_layer(pixel_stack):
	"""Returns first item in list that is a 0 or 1"""
	return [p for p in pixel_stack if p != 2][0]

def decode(digits):
	digits = [int(c) for c in digits]
	layer_size = SIZE[0] * SIZE[1]
	layers = [digits[i: i + layer_size] for i in range(0, len(digits), layer_size)]

	pixels = zip(*layers)
	top_pixels = list(map(top_layer, pixels))

	img = np.array(top_pixels)
	img = img.reshape(SIZE)
	plt.imshow(img)
	plt.show()


digits = read_file()
print("Part one:", part_one(digits))
print("Part two:", decode(digits))