def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    def mul(a):
        return a[0] * a[1]
    
    return sum(list(map(mul, zip(A,B))))
