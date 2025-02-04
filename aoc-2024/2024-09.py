import numpy as np
from copy import copy

# 12345 --> 60


with open("day09.txt") as f:
    disk_map = [int(c) for c in f.read()]

print(disk_map)
def compute_checksum_individual(disk_map: list[int], keep_files_together: bool = False):
    # the verbiage is a little incosistent here
    # "blocks" should really be "files"
    orig_disk_map = copy(disk_map)
    checksum = 0
    cur_block = 0
    cur_pos = 0
    block_ids = [x//2 if x%2==0 else 0 for x in range(len(disk_map))]
    end_block = len(disk_map) - 1

    while True:
        # pairwise
        # first, treat data
        end_of_block_pos = cur_pos + orig_disk_map[cur_block]
        if disk_map[cur_block]:
            # check that this block has not been emptied by being moved
            checksum += block_ids[cur_block] * sum(range(cur_pos, end_of_block_pos))
        cur_block += 1
        cur_pos = end_of_block_pos

        # after treating data, check to see if we've terminated
        if cur_block == len(disk_map):
            return checksum

        # second, treat free space
        start_of_block_pos = cur_pos
        free_block_capacity = disk_map[cur_block]
        if keep_files_together:
            end_scan = len(disk_map) - 1
            while free_block_capacity and end_scan > cur_block:
                # num_data_moved = min(free_block_capacity, disk_map[end_block])
                if disk_map[end_scan] > free_block_capacity:
                    end_scan -= 2
                    continue
            
                num_data_moved = disk_map[end_scan]
                end_of_block_pos = cur_pos + num_data_moved
                checksum += block_ids[end_scan] * sum(range(cur_pos, end_of_block_pos))

                disk_map[end_scan] -= num_data_moved
                cur_pos = end_of_block_pos
                free_block_capacity -= num_data_moved
                # end_block -= 2
                end_scan -= 2
            # whatever happens, move to the end of this block
            cur_pos = start_of_block_pos + disk_map[cur_block]
        else:
            while free_block_capacity and end_block > cur_block:
                num_data_moved = min(free_block_capacity, disk_map[end_block])
                end_of_block_pos = cur_pos + num_data_moved
                checksum += block_ids[end_block] * sum(range(cur_pos, end_of_block_pos))

                disk_map[end_block] -= num_data_moved
                cur_pos = end_of_block_pos
                free_block_capacity -= num_data_moved
                if disk_map[end_block] == 0:
                    end_block -= 2

        cur_block += 1


checksum = compute_checksum_individual(copy(disk_map), keep_files_together=True)
print(f"{checksum=}")