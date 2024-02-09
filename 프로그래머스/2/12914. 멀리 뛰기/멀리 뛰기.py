def solution(n):
    jumpdict = {1:1, 2:2}
    for i in range(3, n+1):
        jumpdict[i] = jumpdict[i-2] + jumpdict[i-1]
    
    return jumpdict[n] % 1234567
