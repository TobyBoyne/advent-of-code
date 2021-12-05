import numpy as np

def bool_arr_to_int(arr):
    return int(''.join(np.where(arr, '1', '0')), 2)

def filter_rating(arr, negate=False):
    for i in range(arr.shape[1]):
        most_common = arr[:, i].sum(axis=0) >= arr.shape[0] / 2
        selection = np.equal(most_common, arr[:, i])
        if negate: selection = np.logical_not(selection)
        arr = arr[selection, :]

        if arr.shape[0] == 1:
            return arr.flat

with open('day03.txt') as f:
    arr = np.array([[int(c) for c in line.strip()] for line in f.readlines()])
    majority = arr.sum(axis=0) > arr.shape[0] / 2
    gamma = bool_arr_to_int(majority)
    epsilon = bool_arr_to_int(~majority)
    print(gamma * epsilon)

    # part two
    oxygen = bool_arr_to_int(filter_rating(arr, negate=False))
    co2 = bool_arr_to_int(filter_rating(arr, negate=True))

    print(oxygen * co2)

    