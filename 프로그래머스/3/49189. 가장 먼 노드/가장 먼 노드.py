def bfs(start, graph, visited):
    
    visited[start] = 1
    q = [start]
    while q:
        s = q.pop(0)
        for adj_v in graph[s]:
            if visited[adj_v] == 0:
                visited[adj_v] = visited[s] + 1
                q.append(adj_v)

    #방문 순서 리스트 리턴
    return visited

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n+1)
    visited = bfs(1, graph, visited)
    
    # 가장 거리가 먼 노드
    max_v = max(visited)
    # 가장 먼 노드들을 수
    count = visited.count(max_v)
    
    return count