# bfs 로 풀이
# 초기 값으로 x와 시도횟수 0으로 시작
# +n *2, *3 을 bfs에 추가하면서
# 시도횟수 +1하기
# 그러다가 값이 같아지면 return
from collections import deque

def solution(x, y, n):
    answer = 0
    q = deque([(x, 0)])
    visited = set()
    while q:
        cur, step = q.popleft()
        
        if cur == y:
            return step
        
        if cur > y or cur in visited:
            continue
        else:
            visited.add(cur)
        
        q.append([cur * 2, step + 1])
        q.append([cur * 3, step + 1])
        q.append([cur + n, step + 1])

    return -1
    