import numpy as np
import re

with open('day02.txt') as f:
    in_text = f.read()
    instructions = {}
    # part one
    for instr in ('forward', 'up', 'down'):
        all_text = re.findall(f'{instr} (\d)', in_text)
        instructions[instr] = np.array(all_text, dtype=int)

    depth = instructions['down'].sum() - instructions['up'].sum()
    horizontal = instructions['forward'].sum()
    print(depth * horizontal)

    # part two
    text_instructions = re.findall(r'(\w*) (\d)', in_text)
    aim = 1 + 0j
    pos = 0 + 0j
    for instr, v in text_instructions:
        v = int(v)
        if instr == 'forward':
            pos += v * aim
        
        else:
            aim += v * (1j if instr == 'down' else -1j)

    print(int(pos.real * pos.imag))
