from collections import Counter
def solution(want, number, discount):
    result = 0
    want = Counter(dict(zip(want, number)))
    shop = []
    for i in discount:
        shop.append(i)
        if len(shop) > 10:
            shop.pop(0)

        if Counter(want) == Counter(shop):
            result += 1
    
    return result