import heapq as hp

def solution(n, workers):
    workers = [-i for i in workers]
    hp.heapify(workers)
    for _ in range(n):
        work = hp.heappop(workers)
        if work < 0:
            hp.heappush(workers, work + 1)
        else:
            hp.heappush(workers, work)
        
    answer = sum([i**2 for i in workers])
    return answer