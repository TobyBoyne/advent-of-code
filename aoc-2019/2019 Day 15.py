import numpy as np
from itertools import cycle

def read_file():
	with open("day15.txt") as f:
		signal = f.read().strip("\n")
	return signal

def gen_patterns(input_length):
	patterns = np.zeros((input_length, input_length))
	base = np.array([0, 1, 0, -1])
	for i in range(input_length):
		seq = base.repeat(i + 1)
		num_repeats = int(np.ceil(input_length / len(seq))) + 1
		patterns[i] = np.tile(seq, num_repeats)[1:input_length + 1]

	return patterns

def clean_signal(signal, n=1):
	patterns = gen_patterns(len(signal))
	signal_arr = np.array([float(c) for c in signal])
	for i in range(n):
		signal_arr = FFT(signal_arr, patterns)

	return "".join(str(int(c)) for c in signal_arr)

def FFT(signal_arr, patterns):
	new_signal = abs(np.sum(patterns * signal_arr, axis=1)) % 10
	return new_signal

SIGNAL = read_file()
out_signal = clean_signal(SIGNAL, 100)
print("Part one:", out_signal[:8])

offset = int(SIGNAL[:7]) % len(SIGNAL)
print("Part two:", out_signal[offset:offset + 8])
