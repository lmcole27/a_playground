n = 3 # n = int(input())
input1 = "4 6"
input2 = "4 8"
input3 = "7 8"

inputs = []
# for x in range(n):
#     #inputs.append(list(map(int, input().split())))    

inputs.append(list(map(int, input1.split())))
inputs.append(list(map(int, input2.split())))
inputs.append(list(map(int, input3.split())))
print(inputs)

# Check if the range 1-7 and 5-5 overlap
smallPointer = inputs[0][0]
largePointer = inputs[0][1]

for i in range(n):
    print(i)
    if smallPointer < inputs[i][0]:
        smallPointer = inputs[i][0]
        # print(smallPointer, inputs[i][0])
    if largePointer > inputs[i][1]:
        largePointer = inputs[i][1]
        # print(largePointer, inputs[i][1])

    if smallPointer > largePointer:
        print("edward is right")
        break

if smallPointer <= largePointer:
    print("gunilla has a point")
# else:
#     print("edward is right")

# print(smallPointer, largePointer)