def solution(n):
    count = 1
    
    for i in range(1, n//2 +1):
        total = 0
        for j in range(i, n+2):
            if total > n:
                break
            elif total == n:
                count += 1
                break
            else:
                total += j

    return count