
class testCase:
    def __init__(self, input, output=0):
        # store the provided input/output instead of discarding them
        self.formattedInput = input.split()
        self.output = output
        self.noHouses = int(self.formattedInput[0])
        #self.houses = list(enumerate(map(int, self.formattedInput[1:self.noHouses+1])))
        #self.garages = list(enumerate(map(int, self.formattedInput[self.noHouses+1:])))
        self.houses = list(enumerate(self.formattedInput[1:self.noHouses+1]))
        self.garages = list(enumerate(self.formattedInput[self.noHouses+1:]))
        self.answer = 0


test1 = testCase(input = """4
3 5 2 7
3 5 2 7""", output = 0)

test2 = testCase("""6
A B C D E F
D C B A F E""", 7)

test3 = testCase("""5
1 3 2 5 4
2 1 3 4 5""", 3)

#testcases = [test1, test2, test3]
testcases = [test1]

def split(list):
    a = list[:(len(list)//2)]
    b = list[(len(list)//2):]
    print(a)
    print(b)

for t in testcases:
    # t.houses.sort(key=lambda x: x[1])
    # t.garages.sort(key=lambda x: x[1])
    print(t.houses)
    print(t.garages)
    split(t.houses)
    split(t.garages)

    for i in range(t.noHouses):
        
        t.answer += abs(t.houses[i][0] - t.garages[i][0])
        # if t.houses[i][0] - t.garages[i][0] > 0:
        #     t.answer += 1
        # elif t.houses[i][0] - t.garages[i][0] < 0:
        #     t.answer += 1
        # else:
        #     pass
    
    # for i in range(t.noHouses-1,0,-1):
    #     #print(f"i = {i}, noHouses = {t.noHouses}")
    #     #print(eval_set[i])
    
    #     if eval_set[i] < eval_set[i-1]:
    #         #print(f"{eval_set[i]} < {eval_set[i-1]}")
    #         t.answer +=1
    #         eval_set[i], eval_set[i-1] = eval_set[i-1], eval_set[i] 
        
    #     if i < t.noHouses-1: 
    #         if eval_set[i] > eval_set[i+1]:
    #             #print(f"{eval_set[i]} > {eval_set[i+1]}")
    #             eval_set[i], eval_set[i+1] = eval_set[i+1], eval_set[i]
    #             t.answer += 1 
    #     for i in range(t.noHouses-1,0,-1):
    #         #print(f"i = {i}, noHouses = {t.noHouses}")
    #         #print(eval_set[i])
        
    #         if eval_set[i] < eval_set[i-1]:
    #             #print(f"{eval_set[i]} < {eval_set[i-1]}")
    #             t.answer +=1
    #             eval_set[i], eval_set[i-1] = eval_set[i-1], eval_set[i] 
            
    #         if i < t.noHouses-1: 
    #             if eval_set[i] > eval_set[i+1]:
    #                 #print(f"{eval_set[i]} > {eval_set[i+1]}")
    #                 eval_set[i], eval_set[i+1] = eval_set[i+1], eval_set[i]
    #                 t.answer += 1 

    #print(f"eval_set = {eval_set}")
    print(f"ans = {t.answer}, expected = {t.output}")
    print(t.answer)