def bfs(start, graph, visited):
    q = [start]
    visited[start] = 1
    while q:
        s = q.pop(0)
        for adj_v in graph[s]:
            if visited[adj_v] == 0:
                visited[adj_v] = visited[s] + 1
                q.append(adj_v)
    
    return visited
    

def solution(n, edge):
    graph= [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n+1)
    visited = bfs(1, graph, visited)
    
    max_v = max(visited)
    answer = visited.count(max_v)
    
    return answer