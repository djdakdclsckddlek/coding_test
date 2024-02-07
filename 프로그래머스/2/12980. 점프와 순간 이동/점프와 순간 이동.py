#
def solution(n):
    result = 1
    while n != 1:
        if n % 2 == 1:
            result += 1
            n -= 1
        else:
            n /= 2

    return result