class Directory:
    def __init__(self, parent:'Directory'=None):
        self.parent = parent
        self.files = []
        self.children: dict[str, 'Directory'] = {}

        self._size = None

    def __repr__(self):
        return f"Dir({self.children})"

    def size(self):
        if self._size is None:
            self._size = sum(self.files) + sum(ch.size() for ch in self.children.values())
        return self._size

    def all_children_iter(self):
        yield self
        for ch in self.children.values():
            yield from ch.all_children_iter()


with open("day07.txt") as f:
    cmds = [*map(str.strip, f.readlines())]

root = Directory()
cd = root
for cmd in cmds:
    if cmd == "$ ls": continue

    if cmd[0] == "$":
        d = cmd.split()[2]
        if d == "..":
            cd = cd.parent
        elif d == "/":
            cd = root
        else:
            cd = cd.children[d]

    else:
        size, name = cmd.split()
        if size == "dir":
            cd.children[name] = Directory(parent=cd)
        
        else:
            cd.files += [int(size)]

print(root)

filtered_total_size = sum(d.size() for d in root.all_children_iter() 
                            if d.size() < 1e5)
print(filtered_total_size)

TOT = 7e7
REQ = 3e7
to_free = REQ - (TOT - root.size())

to_delete = min((d for d in root.all_children_iter() 
                if d.size() > to_free), 
                key=lambda x: x.size())

print(to_delete.size())