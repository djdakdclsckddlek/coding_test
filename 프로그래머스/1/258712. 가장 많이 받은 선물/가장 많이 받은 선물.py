# 가장 많이 받은 선물
from itertools import permutations
def solution(friends, gifts):
    giftpoints = {x : 0 for x in friends}
    nums = {name : 0 for name in permutations(friends, 2)}
    result = [0]  * len(friends)
    for g in gifts:
        giver, receiver = g.split()
        giftpoints[giver] += 1
        giftpoints[receiver] -= 1
        nums[(giver, receiver)] += 1

    for k in range(len(friends)-1):
        
        for i in range(k, len(friends)-1):
            
            p1 = nums[(friends[k], friends[i+1])]
            p2 = nums[(friends[i+1], friends[k])]
            if p1 > p2:
                result[k] += 1
            elif p1 < p2:
                result[i+1] += 1
            else:
                p1_point = giftpoints[friends[k]]
                p2_point = giftpoints[friends[i+1]]
                
                if p1_point > p2_point:
                    result[k] += 1
                elif p1_point < p2_point:
                    result[i+1] += 1
    return max(result)