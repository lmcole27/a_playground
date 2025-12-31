class testCase:
    def __init__(self, input, output=0):
        # store the provided input/output instead of discarding them
        self.formattedInput = input.split()
        self.output = output
        self.n = int(self.formattedInput[0]) # number of elements
        self.d = int(self.formattedInput[1]) # distance a hopper can jump in no of elements
        self.m = int(self.formattedInput[2]) # magnitude of change a hopper can tolerate
        self.elements = self.formattedInput[3:self.n+3]
        self.eInt = [int(i) for i in self.elements]
        self.answer = 0

test1 = testCase(input = """8 3 1
1 7 8 2 6 4 3 5""", output = 8)

test2 = testCase(input = """8 2 1
1 7 8 2 6 4 3 5""", output = 3)

test3 = testCase(input = """8 1 1
1 7 8 2 6 4 3 5""", output = 1)

#testcases = [test1, test2, test3]
testcases = [test1]                                             

for t in testcases:
    options = []
    jump = []
    x = t.d
    while x > 0:
        jump.append(x)
        jump.append(-x)
        x -= 1
    print(f"jump = {jump}")
# two pointers?
    for i in range(t.n):
        print(f"i = {i}")
        print(f"element = {t.eInt}")
        # create a jump list if d = 1 jump = [1,-1]
        # if d = 3 jump = [1,2,3,-1,-2,-3]        
        for j in jump:
            # check this condition more carefully
            if i + j <= t.n -1 and i + j >=0:
        #what are the options from position i:

                if t.eInt[i] - t.eInt[j] >= t.m:
                    print(t.eInt[i],t.eInt[j], t.m)
                    path = (t.eInt[i], t.eInt[j])
                    options.append(path)
    print(t.output, options)

