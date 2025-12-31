

# input = "A2B1A2B2B8B8A1A2A2A2"
# output = "A"

input = "A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2"
output = "A"

input = list(input)
print(input)
scoreA = 0
scoreB = 0

for i in range(len(input)):
    if i % 2 == 0:
        pass
    #print(i)
    if input[i] == "A":
        scoreA += int(input[i+1])
    elif input[i] == "B":
        scoreB += int(input[i+1])
print(f"scoreA = {scoreA}, scoreB = {scoreB}")

if scoreA < 10 or scoreB < 10:
    if scoreA > scoreB:
        print("A")
    elif scoreB > scoreA:
        print("B")
else:
    if scoreA - scoreB >=2:
        print("A")
    else:
        print("B")
