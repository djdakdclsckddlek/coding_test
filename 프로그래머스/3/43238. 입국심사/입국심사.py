# 이분탐색  왼쪽 오른쪽 오차를 줄여나가면서 찾기
def solution(n, times):
    answer = 0
    
    # 최소 최대
    left, right = 1, times[-1] * n
    
    #오차 줄여나가기
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid -1
        elif people < n:
            left = mid +1
    
    return left
        
        