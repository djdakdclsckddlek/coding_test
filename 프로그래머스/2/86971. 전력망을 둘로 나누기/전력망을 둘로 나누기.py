def dfs(start, graph, visited, check_link):
    cnt = 1
    visited[start] = True            # 시작 노드 방문
    for adj_v in graph[start]:      # 시작 노드에 연결되어있는 다들 노드들
        #연결된 노드가 방문한적 없고 
        if visited[adj_v] == False and check_link[start][adj_v]:  
            cnt += dfs(adj_v, graph, visited, check_link)
    
    return cnt

def solution(n, wires):
    answer = n
    
    # 끊은 간선인지 아닌지 체크하는 리스트
    check_link = [[True] * (n+1) for _ in range(n+1)]
    # 송전탑 그래프
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n+1)                   # 간선 정보를 다 확인하면서
        check_link[a][b] = False                    # a에서 b 그룹의 붙어있는 송전탑 개수를 세기위해
        cnt_a = dfs(a, graph, visited, check_link)  # a랑 붙어있는 송전탑 개수
        cnt_b = dfs(b, graph, visited, check_link)  # b랑 붙어있는 송전탑 개수
        check_link[a][b] = True                     # 끊은 간선 다시 연결
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer