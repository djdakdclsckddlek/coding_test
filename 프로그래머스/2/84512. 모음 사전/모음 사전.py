from itertools import product

def solution(word):
    abc = 'AEIOU'
    arr1 = []
    for i in range(1, 6):
        for j in product(abc, repeat=i):
            arr1.append(''.join(list(j)))
    arr1.sort()

    return arr1.index(word)+1