# 크루스칼 알고리즘

def solution(n, costs):
    
    costs.sort(key = lambda x: x[2])
    answer = 0
    link = set([costs[0][0]])
    
    while len(link) != n:
        for start, end, cost in costs:
            if start in link and end in link:
                continue
            
            if start in link or end in link:
                answer += cost
                link.update([start, end])
                break
            
    return answer