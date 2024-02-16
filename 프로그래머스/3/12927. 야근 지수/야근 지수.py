import heapq as hp

def solution(n, workers):
    if n >= sum(workers):
        return 0
    workers = [-i for i in workers]
    
    hp.heapify(workers)
    for _ in range(n):
        work = hp.heappop(workers)
        if work < 0:
            hp.heappush(workers, work + 1)
        
    answer = sum([i**2 for i in workers])
    return answer