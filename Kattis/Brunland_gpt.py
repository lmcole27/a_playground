
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

#testcases = [test1, test2, test3]
testcases = [test4]

def count_inversions(arr):
    if len(arr) <= 1:
        return 0, arr
    
    mid = len(arr) // 2
    print(f"arr = {arr}, mid = {mid}")
    left_inv, left = count_inversions(arr[:mid])
    right_inv, right = count_inversions(arr[mid:])
    print(f"""left_inv = {left_inv}, left = {left}, \nright_inv = {right_inv}, right = {right}\n""")
    
    i = j = 0
    merged = []
    inv = left_inv + right_inv
    print(f"inv = {inv} before merging")

    while i < len(left) and j < len(right):
        print(f"while loop i = {i}, j = {j}, left[i] = {left[i]}, right[j] = {right[j]}")
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
            print(f"merged = {merged} after adding left, inv = {inv}")
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i   # all remaining left elements form inversions
            print(f"merged = {merged} after adding right, inv = {inv}")
    merged.extend(left[i:])
    print(f"merged = {merged} after extending left, inv = {inv}")
    merged.extend(right[j:])
    print(f"merged = {merged} after extending right, inv = {inv}\n")
    return inv, merged



for t in testcases:
    garages = t.garages
    houses = t.houses
    pos = {}
    for i, g in enumerate(garages):
        pos[g] = i
    seq = [pos[h] for h in houses]
    seq2 = []
    for h in houses:
        print(f"h = {h}, pos[h] = {pos[h]}")
        seq2.append(pos[h])
    print(pos)
    print(seq)

    inversions, _ = count_inversions(seq)
    print(f"inversions {inversions}, _ = {_}")




