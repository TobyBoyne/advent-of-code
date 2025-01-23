with open("day18.txt") as f:
    voxels = [tuple(map(int, line.split(","))) for line in f.readlines()]

def get_faces(v):
    x, y, z = v
    return {
        (x,    y+.5, z+.5),
        (x+1,  y+.5, z+.5),
        
        (x+.5, y,    z+.5),
        (x+.5, y+1,  z+.5),
        
        (x+.5, y+.5, z),
        (x+.5, y+.5, z+1),
    }

all_faces = set()
duplicated_face_count = 0

for v in voxels:
    faces = get_faces(v)
    overlap = all_faces & faces
    duplicated_face_count += len(overlap)
    all_faces |= faces
    all_faces ^= overlap
    

print(len(all_faces))

start = min(all_faces, key=lambda x: x[0])

ds = ((1, 1), (1, -1), (-1, -1), (-1, 1))

def explore(face):
    pass