#sent = list(input().split())
import sys
lines = [
    "baby shark",
    "doo doo doo doo doo doo",
    "baby shark, doo doo doo doo doo doo",
    "baby shark, doo doo doo doo doo doo",
    "baby shark shark doo doo doo shark shark"
]

for line in lines:
    sent = list(line.split())
    #print(f"sent = {sent}")

    ans = ""
    highestCount = 0
    currentCount = 1
    currentWord = ""
    lastWord = ""
    # dict = {}

    for i in range(len(sent)):
        currentWord = sent[i].strip(".,!?;\"'()[]{}")
        
        if currentWord == lastWord:
            currentCount += 1    
        
        elif ans == "":
            ans = currentWord
            highestCount = 1
            lastWord = currentWord
        
        else:
            currentCount = 1
            lastWord = currentWord

        if currentCount > highestCount:
            ans = currentWord
            highestCount = currentCount

    print(ans)
    #print(f"ANSWER: {ans}")

    # max_value = max(dict, key=dict.get)
    #print(max_value)