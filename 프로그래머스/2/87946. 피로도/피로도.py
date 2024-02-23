answer = 0
def dfs(k, visited, depth, dungeons):
    global answer
    if depth > answer:
        answer = depth
    #방문하지 않았고, 최소 요규 피로도 이상일 때
    for i in range(len(dungeons)):
        if visited[i] == 0 and dungeons[i][0] <= k:
            # 방문처리 및 깊이 늘려서 반복
            visited[i] = 1
            dfs(k-dungeons[i][1], visited, depth + 1, dungeons)
            # 다음을 위해 방문처리 취소
            visited[i] = 0

def solution(k, dungeons):
    # 방문 횟수 배열에서 
    # dfs로 방문하면서 가장 많이 방문한 횟수 리턴
    visited = [0] * len(dungeons)
    global answer
    
    # k, 방문여부, 깊이, 던전
    dfs(k, visited, 0, dungeons)
    
    return answer

        