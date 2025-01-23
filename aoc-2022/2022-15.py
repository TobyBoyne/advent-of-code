from parse import parse

# ---
def union(I):  
   
    I = sorted(I, key=lambda interval: interval[0])
    new_intervals = I
    # print(new_intervals)
    merge_flag = True
    while merge_flag:
        merge_flag = False
        I = new_intervals
        new_intervals = []
        
        # use while loop so that i can be manually increased
        i = 0
        while i < len(I):
            if i == len(I) - 1:
                # don't lose final interval!
                new_intervals += [I[i]]
            
            else:
                (a1, b1), (a2, b2) = I[i:i+2]
                # no overlap
                if a2 > b1:
                    new_intervals += [[a1, b1]]

                # some overlap
                if a2 <= b1:
                    merge_flag = True
                    new_intervals += [[a1, max(b1, b2)]]
                    i += 1 # skip next interval
                    
            i += 1
                    
    return I
                
            
            
# ---


with open("day15.txt") as f:
    readings = []
    for line in f.readlines():
        p = parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line.strip())
        readings += [p.fixed]


SCAN_LINE = 2000000
beacons = set()
intervals = []
for reading in readings:
    sx, sy, bx, by = reading
    scan_range = abs(by - sy) + abs(bx - sx)
    scan_width = max(scan_range - abs(SCAN_LINE - sy), -1)
    if by == SCAN_LINE:
        beacons.add((bx, by))
    if scan_width > -1:
        interval = [sx - scan_width, sx + scan_width]
        intervals.append(interval)

print(intervals)
intervals = union(intervals)
print(intervals)
beacon_count = len(beacons)
print(sum(i[1] - i[0] + 1 for i in intervals) - beacon_count)