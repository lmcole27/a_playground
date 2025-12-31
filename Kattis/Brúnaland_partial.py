
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

testcases = [test1, test2, test3]

for t in testcases:
    mylist = []
    ans = 0
    result = 0
    for i in range(t.noHouses):
        garageindex = t.garages.index(t.houses[i])
        mylist.append((i,garageindex))
        x1 = mylist[i][0]
        x2 = mylist[i][1]        
        for z in range(0, i):
            x3 = mylist[z][0]
            x4 = mylist[z][1]

            divisor = -(x2-x1)+(x4-x3) #check if divisor = 0
            if divisor != 0:
                result = (x1 - x3) / divisor 
                print(f"{mylist[i]} {mylist[z]} {result}")
                if 0<=result<=1:
                    ans +=1
            else:
                print(f"{mylist[i]} {mylist[z]} divisor = 0")

    print(t.output, ans)


    # for i in range(t.noHouses):
    #     garageindex = t.garages.index(t.houses[i])
    #     mylist.append((i,garageindex))


    # for i in range(t.noHouses):
    #     for z in range(i+1, t.noHouses):
    #         x1 = mylist[i][0]
    #         x2 = mylist[i][1]
    #         x3 = mylist[z][0]
    #         x4 = mylist[z][1]

    #         divisor = -(x2-x1)+(x4-x3) #check if divisor = 0
    #         if divisor != 0:
    #             result = (x1 - x3) / divisor 
    #             print(f"{mylist[i]} {mylist[z]} {result}")
    #             if 0<=result<=1:
    #                 ans +=1
    #         else:
    #             print(f"{mylist[i]} {mylist[z]} divisor = 0")

    # print(t.output, ans)
    # print(t.formattedInput)
    # print(t.noHouses)
    # print(t.houses)
    # print(t.garages)   
    # print("-----")

    # for i in range(t.noHouses):
    #     print(f"i={i}")
    #     garageindex = t.garages.index(t.houses[i])
    #     if garageindex - i < 0:
    #         t.answer += abs(garageindex - i + 1)
    #     else:
    #         t.answer += garageindex - i
    #     print(f"testcase {t.noHouses} = {t.answer}")
    # print(f"{t.noHouses} {t.answer} = {t.output}")

    # stringsList = ["1", "2", "3"]
    # numbersList = list(map(int, stringsList))
    # print(numbersList)
    # print("=========")



#for coordinates in mylist:
