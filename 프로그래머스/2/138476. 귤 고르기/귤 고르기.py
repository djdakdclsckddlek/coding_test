from collections import Counter
def solution(k, tangerine):
    arr = Counter(tangerine).most_common()
    count = 0
    while k > 0:
        k -= arr[count][1]
        count += 1
    return count