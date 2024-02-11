def solution(prices):
    result = []
    
    for i in range(len(prices)-1):
        time = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]:
                time += 1
            else:
                break
        
        result.append(time)
    
    result.append(0)
    return result