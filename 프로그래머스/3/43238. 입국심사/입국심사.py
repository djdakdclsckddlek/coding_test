def solution(n, times):
    answer = 0
    # 최소, 최대 시간을 설정하고 mid를 줄여나가면서 시간을 맞추기
    left, right = 1, times[-1] * n
    
    while left <= right:
        mid = (left + right ) // 2
        people = 0
        
        for time in times:
            # 모든 심사관이 mid분 동안 심사한 사람의 수
            people += mid // time
            
            if people >= n:
                break
        
        # n명 보다 같거나 많이 심사할 수 있는경우
        if people >= n:
            answer = mid
            right = mid -1
        # n명 보다 적게 심사하는 경우
        elif people < n:
            left = mid +1
    
    return answer