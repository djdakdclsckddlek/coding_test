import heapq as hp

def solution(scoville, K):
    hp.heapify(scoville) #리스트를 힙 자료형으로 만글기
    count = 0
    
    while scoville[0] < K:
        count += 1
        
        min_1 = hp.heappop(scoville)
        min_2 = hp.heappop(scoville)
        hp.heappush(scoville, min_1 + min_2 *2)

        if len(scoville) == 2 and (scoville[0] + scoville[1] * 2) < K:
            return -1 
    return count