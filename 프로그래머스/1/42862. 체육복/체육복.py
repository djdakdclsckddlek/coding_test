def solution(n, lost, reserve):
    a1, a2 = set(lost), set(reserve)
    lost = list(a1 - a2)
    reserve = list(a2 - a1)
    
    answer = 0
    for los in lost:
        if los - 1 in reserve:
            reserve.remove(los-1)
            answer += 1
        elif los + 1 in reserve:
            reserve.remove(los + 1)
            answer += 1
    return n - len(lost) + answer

print(solution(5, [4, 5], [3, 4]))