def solution(n, times):
    answer = 0
    
    left, right = 1, times[-1] * n
    
    # left right 차이가 줄어들다가
    # 정답을 맞추면(left = right되는순간) right가 mid-1이되고
    # 그순간 left > right가 되서 반복문을 나오고
    # left가 정답임으로 left return 
    
    while left <= right:
        people = 0
        mid = (left + right) // 2
        for time in times:
            
            people += mid // time
            
            if people >= n:
                break
        
        if people >= n:
            right = mid -1
        elif people < n:
            left = mid + 1
            
    return left