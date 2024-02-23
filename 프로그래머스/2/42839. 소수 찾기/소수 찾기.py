from itertools import permutations
def solution(numbers):
    arr = []
    answer = 0
    
    def isprime(n):
        return False if n == 0 or n == 1 or any([n % i == 0 for i in range(2, int(n**0.5)+1)]) else True
    
    for i in range(1, len(numbers)+1):
        arr.extend(list(map(''.join, permutations(numbers, i))))
    
    arr = list(map(int, arr))
    for nums in set(arr):
        if isprime(int(nums)):
            answer += 1
            print(nums)
    
    return answer