
class testCase:
    def __init__(self, input, output=0):
        # store the provided input/output instead of discarding them
        self.formattedInput = input.split()
        self.output = output
        self.noHouses = int(self.formattedInput[0])
        self.houses = self.formattedInput[1:self.noHouses+1]
        self.garages = self.formattedInput[self.noHouses+1:]
        self.answer = 0


test1 = testCase(input = """7
3 5 2 7 6 4 1
3 5 2 7 6 4 1""", output = 0)

test2 = testCase("""4
1 2 3 4
4 3 2 1""", 6)

test3 = testCase("""5
1 3 2 5 4
2 1 3 4 5""", 3)

test4 = testCase("""2
1 2
2 1""", 1)

testcases = [test1, test2, test3]


# Fenwick Tree / Binary Indexed Tree (0-based wrapper)
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)  # internal 1-based

    def add(self, idx, delta):
        # idx is 0-based externally
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, idx):
        # sum of [0..idx], idx is 0-based
        if idx < 0:
            return 0
        s = 0
        i = idx + 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s



for t in testcases:
    n = t.noHouses
    houses = t.houses
    garages = t.garages

    # Map garage number -> its index on the top side
    pos = {g: i for i, g in enumerate(garages)}

    # Build sequence of garage indices in house order
    seq = [pos[h] for h in houses]

    ans = 0
    bit = BIT(n)

    # Traverse from right to left
    for v in reversed(seq):
        # How many elements smaller than v have we already seen?
        ans += bit.prefix_sum(v - 1)
        # Mark v as seen
        bit.add(v, 1)

    print(ans)