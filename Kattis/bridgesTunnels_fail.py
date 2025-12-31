data = []
dataSetsToMerge = []
ans = 0
no = 9 #int(input())
connectors = ["MC DC", "DC Eng", "MC MThree", "BUS MED", "AD BC", "LMC MMC", "BC LMC", "LMC DC", "DC MED"] # "DC MED" - after BUS MED

for n in range(no):
    conn = connectors[n].split() #conn = input().split()

    if len(data) == 0:
        data.append(set(conn))
        data[0].add(conn[0])
        data[0].add(conn[1])
        ans = len(data[0])
        print(f"LOOP {n} ANSWER : {data}, {ans}")

    elif len(data) == 1:
            if conn[0] in data[0] or conn[1] in data[0]:
                data[0].add(conn[0])
                data[0].add(conn[1])
                ans = len(data[0])
            else:
                data.append(set(conn))
                ans = len(data[1])
            print(f"LOOP {n} ANSWER : {data}, {ans}")

    else:
        newData = data
        for i in range(0, len(data)):
            if (conn[0] in data[i] or conn[1] in data[i]):
                dataSetsToMerge.append(i)

            if len(dataSetsToMerge) == 2:
                break

        if len(dataSetsToMerge) == 0:
            data.append(set(conn))
            ans = len(data[-1])
   
        else:
            # I assume that they will always be merged into the first found set
            for j in range(1, len(dataSetsToMerge)):
                newData[dataSetsToMerge[0]] = newData[dataSetsToMerge[0]].union(newData[dataSetsToMerge[j]])
                #print(dataSetsToMerge, len(dataSetsToMerge), data, newData)
            for j in range(len(dataSetsToMerge)-1, 1, -1):
                newData.pop(dataSetsToMerge[j])
            ans = len(newData[dataSetsToMerge[0]])
        dataSetsToMerge = []
        data = newData
        print(f"LOOP {n} ANSWER : {data}, {ans}")
