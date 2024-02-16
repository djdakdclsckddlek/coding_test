from collections import deque

def bfs(maps, start):
    q = deque()
    dx = [0, 1, 0 , -1]
    dy = [1, 0, -1, 0]
    q.append(start)
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            nx = now_r + dx[i]
            ny = now_c + dy[i]
            
            if not(0 <= nx < len(maps) and 0 <= ny < len(maps[0])):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[now_r][now_c] + 1
                q.append((nx, ny))
    
    return maps

def solution(maps):
    start = [0,0]
    maps = bfs(maps, start)
    
    end = maps[len(maps)-1][len(maps[0])-1]
    if end == 1:
        return -1
    return end