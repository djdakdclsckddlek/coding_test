def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1set = set()
    str2set = set()
    str1dict = dict()
    str2dict = dict()
    result1 = 0
    result2 = 0
    
    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            str1set.add(str1[i]+str1[i+1])

            if str1[i]+str1[i+1] in str1dict:
                str1dict[str1[i]+str1[i+1]] += 1
            else:
                str1dict[str1[i]+str1[i+1]] = 1

    for i in range(len(str2)-1):
        if (str2[i] + str2[i+1]).isalpha():
            str2set.add(str2[i] + str2[i+1])

            if str2[i]+str2[i+1] in str2dict:
                str2dict[str2[i]+str2[i+1]] += 1
            else:
                str2dict[str2[i]+str2[i+1]] = 1

    교집합 = str1set & str2set
    합집합 = str1set | str2set
    
    if len(합집합) == 0:
        return 65536
    elif len(교집합) == 0:
        return 0
    print(교집합, 합집합)
    
    
    for i in 교집합:
        result1 += min(str1dict[i], str2dict[i])
    for i in 합집합:
        pass
        if i in str1dict and i in str2dict:
            result2 += max(str1dict[i], str2dict[i])
        elif i in str1dict:
            result2 += str1dict[i]
        elif i in str2dict:
            result2 += str2dict[i]
            
    print(result1, result2)
    return  int(result1 / result2 * 65536)