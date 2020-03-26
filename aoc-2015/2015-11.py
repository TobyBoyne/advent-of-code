import numpy as np

# i, l, o all banned
banned = {8, 11, 14}

class Password:
	def __init__(self, initial_password):
		self.pass_arr = np.array([ord(c) for c in initial_password]) - 97

	def next_valid_password(self):
		self.next_no_banned()
		while not self.valid_pass():
			self.increment()
			self.next_no_banned()

	def increment(self, idx=-1):
		self.pass_arr[idx] += 1
		if self.pass_arr[idx] > 25:
			carry, self.pass_arr[idx] = divmod(self.pass_arr[idx], 26)
			self.increment(idx - 1)


	def next_no_banned(self):
		# find the next password that does not contain any of the banned letters
		# edits list in place
		for i, c in enumerate(self.pass_arr):
			if c in banned:
				self.pass_arr[i] += 1
				self.pass_arr[i + 1:] = 0

	def valid_pass(self):
		repeat_pairs = np.nonzero(np.diff(self.pass_arr) == 0)
		unique_pairs = np.unique(self.pass_arr[repeat_pairs])

		consecutive = np.nonzero(np.diff(self.pass_arr) == 1)
		straight_count = np.count_nonzero(np.diff(consecutive) == 1)

		return len(unique_pairs) >= 2 and straight_count >= 1

	def __repr__(self):
		return "".join(chr(c) for c in self.pass_arr + 97)


def part_one(old_pass_str):
	password = Password(old_pass_str)
	password.next_valid_password()
	print(password)


old_password = "vzbxkghb"
part_one(old_password)