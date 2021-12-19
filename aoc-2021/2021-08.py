from collections import Counter
import numpy as np

segments = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

inverse_segments = {v: k for k, v in segments.items()}

freqs = Counter(''.join(segments.values()))

with open('day08.txt') as f:
    lines = f.readlines()
    entries = [ [sub.split() for sub in line.split(' | ')] for line in lines]


def part_one():
    unique_counts = 0
    for entry in entries:
        unique_counts += sum(len(s) in (2, 3, 4, 7) for s in entry[1])

    return unique_counts


def mapping_to_dict(mapping):
    """If mapping is one-to-one, return dictionary of wire to segment
    otherwise return None"""
    # in case the mapping isn't invertible (it will be!)
    if not ( np.all(mapping.sum(axis=0) == 1) and np.all(mapping.sum(axis=1) == 1) ):
        return None
    
    W, S = np.nonzero(mapping)
    mapping_dict = {chr(s + ord('a')): chr(w + ord('a')) for w, s in zip(W, S)} 

    return mapping_dict


def decode(digits, code):
    mapping = np.ones((7, 7)) # [wire, segment] index
    
    # first, find the segments that have the same frequency counts for unique counts
    # i.e. {'f': 9, 'b': 6, 'e': 5}
    entry_freqs = Counter(''.join(digits))

    for k in ('f', 'b', 'e'):
        unique_count = next(filter(lambda i: entry_freqs[i] == freqs[k], 'abcdefg'))

        i_wire = ord(k) - ord('a')
        i_seg = ord(unique_count) - ord('a')

        mapping[i_wire, :] = 0
        mapping[:, i_seg] = 0
        mapping[i_wire, i_seg] = 1
        
    # then, find uniquely decodable digits with unique segment counts
    for x in (1, 4, 7, 8):
        unique_digit = next(filter(lambda i: len(i) == len(segments[x]), digits))
        mask = np.ones_like(mapping)

        i = tuple(ord(c) - ord('a') for c in segments[x])
        j = tuple(ord(c) - ord('a') for c in unique_digit)

        mask[i, :] = 0
        mask[:, j] = 0
        mask[np.ix_(i, j)] = 10

        mapping = np.logical_and(mapping, mask)

    # should have enough information for a unique map
    mapping_dict = mapping_to_dict(mapping)
    
    # find code using map
    decoded = ''
    for c in code:
        wires = ''.join( sorted(map(mapping_dict.get, c)) )
        d = inverse_segments[wires]
        decoded += str(d)

    return int(decoded)


def part_two():
    return sum(decode(digits, code) for digits, code in entries)

print(part_one())
print(part_two())
