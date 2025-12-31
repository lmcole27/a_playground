def ransomCompare():
    magazine = "aab"
    ransomnote = "aa"
    ransomDic = {}
    magazineDic = {}

    for letter in magazine:
        if letter in list(magazineDic.keys()):
            magazineDic[letter] += 1
        else:
            magazineDic[letter] = 1

    for letter in ransomnote:
        if letter in list(ransomDic.keys()):
            ransomDic[letter] += 1
        else:
            ransomDic[letter] = 1
        print(list(magazineDic.keys()))
        if letter in list(magazineDic.keys()):
            if ransomDic[letter] > magazineDic[letter]:
                return False
            # print(letter)
            # print(ransomDic[letter])
            # print(magazineDic[letter])
            # print(magazineDic)
            # print(letter)
        else:
            return False
    return True


print(ransomCompare())