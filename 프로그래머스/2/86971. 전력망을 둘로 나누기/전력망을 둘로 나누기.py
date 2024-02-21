def dfs(start, visited, graph, check_link):
    cnt = 1
    visited[start] = 1
    
    for adj_v in graph[start]:
        if visited[adj_v] == 0 and check_link[start][adj_v]:
            visited[adj_v] = 1
            cnt += dfs(adj_v, visited, graph, check_link)
    
    return cnt

    
def solution(n, wires):
    # 그래프랑 연결여부 체크하고
    # 연결 끊어보면서 연결된 송전망 개수차이 새기
    graph = [[] for _ in range(n+1)]
    check_link = [[True] * (n+1) for _ in range(n+1)]
    answer = 100
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a,b in wires:
        visited = [0] * (n+1)
        check_link[a][b] = False
        cnt_a = dfs(a, visited, graph, check_link)
        cnt_b = dfs(b, visited, graph, check_link)
        check_link[a][b] = True
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer
        