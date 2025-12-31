import sys

#no = sys.stdin.readline

no = 9
connectors = ["MC DC", "DC Eng", "MC MThree", "BUS MED", "AD BC", "LMC MMC", "BC LMC", "LMC DC", "DC MED"] # "DC MED" - after BUS MED
parent = {}
size = {}

def find(x):
    # Initialize if new
    if x not in parent:
        parent[x] = x
        size[x] = 1
        return x
    # Path compression
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return size[ra]

    # Union by size: attach smaller to larger
    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]
    return size[ra]

ans = 0

for _ in range(no):
    u, v = connectors[_].split()
    #u, v = sys.stdin.readline().split()

    ans = union(u, v)

    print(ans)

#sys.stdout.write(ans)