n = 3
input1 = "1 2 3 4 5 6"
input2 = "7 6 5 4 3 2"

win = 0
#n = int(input())
first = list(map(int, input1.split()))
second = list(map(int, input2.split()))
first.sort()
second.sort()
#print(first, second)

for s in first:
    for x in second:
        if s > x:
            win +=1
        elif s < x:
            win -= 1

#print(win)

if win == 0:
    print("tie")
elif win > 0:
    print("first")
else:
    print("second")