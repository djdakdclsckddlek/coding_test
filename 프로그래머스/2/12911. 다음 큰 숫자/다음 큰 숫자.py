def solution(n):
    n1_count = str(bin(n)).count('1')
    
    while 1:
        n += 1
        n2_count = str(bin(n)).count('1')
        if n1_count == n2_count:
            return n
    