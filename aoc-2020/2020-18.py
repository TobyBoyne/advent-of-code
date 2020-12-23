from operator import add, mul

with open('day18.txt') as f:
	expressions = [l.rstrip() for l in f.readlines()]

OP_FUNCS = {'+': add, '*': mul}

def resolve_left_to_right(nums, ops):
	while len(nums) > 1:
		a, b = nums.pop(0), nums.pop(0)
		result = ops.pop(0)(a, b)
		nums.insert(0, result)


def resolve_add_before_mul(nums, ops):
	mul_stack = []
	while len(nums) > 1:
		op = ops.pop(0)
		if op == add:
			a, b = nums.pop(0), nums.pop(0)
			result = op(a, b)
			nums.insert(0, result)
		elif op == mul:
			a = nums.pop(0)
			mul_stack.insert(0, a)

	while len(mul_stack) > 0:
		a, b = nums.pop(0), mul_stack.pop(0)
		result = mul(a, b)
		nums.insert(0, result)



def eval_expression(s, resolve_func):
	first_paren = s.find('(')
	if first_paren == -1:
		# resolve expression
		# build up operation stack
		nums = []
		ops = []
		token = ''
		for i, c in enumerate(s.replace(' ', '')):
			if c in '+*':
				nums.append(int(token))
				ops.append(OP_FUNCS[c])
				token = ''
			else:
				token += c
		nums.append(int(token))

		# resolve stack
		resolve_func(nums, ops)

		return str(nums[0])

	else:
		# resolve parentheses
		depth = 0
		for i in range(first_paren, len(s)):
			if s[i] == '(':
				depth += 1
			if s[i] == ')':
				depth -= 1
				if depth == 0:
					break

		else: # nobreak
			raise ValueError('Mismatched parens')

		expanded_s = s[:first_paren] + eval_expression(s[first_paren + 1:i], resolve_func) + s[i+1:]
		return eval_expression(expanded_s, resolve_func)


def part_one():
	f = resolve_left_to_right
	return sum(int(eval_expression(e, f)) for e in expressions)

def part_two():
	f = resolve_add_before_mul
	return sum(int(eval_expression(e, f)) for e in expressions)


print('Part one', part_one())
print('Part two', part_two())