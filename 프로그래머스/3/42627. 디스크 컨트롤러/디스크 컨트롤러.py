import heapq as hp
def solution(jobs):
    answer = 0
    start, time = -1, 0
    done = 0
    heap = []
    
    while done < len(jobs):
        
        # 가능한거 추가
        for i in range(len(jobs)):
            if start < jobs[i][0] <= time:
                hp.heappush(heap, [jobs[i][1], jobs[i][0]])
        
        # 가능한거있으면 가장 빠르게 진행할수있는것 부터 시간추가
        if heap:
            now = hp.heappop(heap)
            start = time
            time += now[0] 
            
            answer += (time - now[1])
            done += 1
        #업승면 시간 +1
        else:
            time += 1
    return answer // len(jobs)