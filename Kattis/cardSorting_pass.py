import datetime

input = 7
cards = ["Graedgiskrukka, 55144522, Galdur - Venjulegur, 2004-03-01", 
"Afsaladur, 64631466, Skrimsli - Bodunar, 2004-10-12",
"Ojama toki, 00000000, Annad, 2017-07-01",
"Alvarlegur domur, 41420027, Gildra - Mot, 2004-12-01",
"OrlogsHETJA Demantagaur, 13093792, Skrimsli - Ahrifa, 2006-05-17",
"Sa bannadi, 33396948, Skrimsli - Ahrifa, 2004-10-12",
"Kvenharpiasystur, 12206212, Skrimsli - Ahrifa, 2004-10-12"]

data = []

typeScore = {
    "Skrimsli":{"":19,"Venjulegt" : 11, "Ahrifa": 12,"Bodunar": 13, "Samruna": 14, "Samstillt": 15, "Thaeo": 16, "Penduls": 17, "Tengis":  18}, 
    "Galdur":{"":29,"Venjulegur": 21,"Bunadar":22, "Svida":23, "Samfelldur":24, "Bodunar":25, "Hradur":26},
    "Gildra":{"":39,"Venjuleg":31,"Samfelld":32, "Mot":33},
    "Annad" : {"":40}
    }

noCards = 7 #int(input())

for i in range(noCards):
    card = cards[i].split(",") #card = input()
    #card = card.split(",")
    
    name = card[0].strip()
    #name = name.strip()
    
    id = int(card[1])

    catList = card[2].split("-")
    cat = catList[0]
    cat = cat.strip()
    if len(catList) == 1:
        subCat = ""
    else:
        subCat = catList[1]
        subCat = subCat.strip()

    date = (card[3])
    year = int(date[0:5])
    month = int(date[6:8]) 
    day = int(date[9:11])
    dateFormatted = datetime.datetime(year, month, day)

    data.append([ name, id, typeScore[cat][subCat], dateFormatted])



# df = pd.DataFrame(data, columns=column_names)
# df = df.sort_values(by=sortOrder)
# print(df)

# for index, row in df.iterrows():
#     print(row['nafn'])


#for i in range(len(data)):

sortItem = {'nafn':0, 'id':1, 'flokkur':2,'dagsetning':3}

#sortOrder = "nafn id flokkur dagsetning"
# sortOrder = "flokkur dagsetning nafn id"
sortOrder = "dagsetning flokkur id nafn" #input()
sortOrder = sortOrder.split()


newData = sorted(data, key=lambda x: (x[sortItem[sortOrder[0]]], x[sortItem[sortOrder[1]]],x[sortItem[sortOrder[2]]],x[sortItem[sortOrder[3]]]))
# print(newData)

for i in range(noCards):
    # print(newData[i][0], newData[i][1], newData[i][2], newData[i][3].strftime("%Y-%m-%d"))
    print(newData[i][0])