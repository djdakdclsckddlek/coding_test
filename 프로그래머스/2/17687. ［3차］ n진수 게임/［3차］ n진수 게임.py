def solution(n, t, m, p):
    result = ''
    #n 진수 변환
    def convert(n, k):
        if n == 0:
            return '0'
        
        T = '0123456789ABCDEF'
        tmp = ''
        while n > 0:
            n, r = divmod(n, k)
            tmp = T[r] + tmp
        return tmp
    
    word = ''
    level = 0
    while len(word) < t * m:
        word += convert(level,n)
        level += 1
    
    # 말하는 순서에 따라 더하기 이것만 해결하면되는데 i가 p가 될때
    for i in range(len(word)):
        if i % m == p-1 and i < t*m:
            result += word[i]

    return result