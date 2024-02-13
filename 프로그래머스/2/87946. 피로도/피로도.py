N = 0
answer = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
        
    for j in range(N):
        
        if k >= dungeons[j][0] and visited[j] == 0:
            visited[j] = 1 # 방문하려는 곳 1체크
            dfs(k-dungeons[j][1], cnt+1, dungeons)
            visited[j] = 0 # 뒤로가려는 경우 0으로 다시 돌려놓기


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer