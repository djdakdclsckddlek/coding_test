def solution(n, k):
    T = '0123456789ABCDEF'
    tmp = ''
    result = 0
    
    while n > 0:
        n, r = divmod(n, k)
        tmp = T[r] + tmp
        
    numbers = [int(num) for num in tmp.split('0') if num]
    for n in numbers:
        n = int(n)
        if not (n == 1 or any([n % i == 0 for i in range(2, int(n**0.5) +1)])):
            result += 1
            
    return result