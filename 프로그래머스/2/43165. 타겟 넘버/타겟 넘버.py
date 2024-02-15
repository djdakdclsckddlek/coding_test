answer = 0
N = 0
visited = []

def dfs(numbers, target, depth):
    global answer

    if depth == N:  # 종료 조건: 모든 숫자를 다 방문한 경우
        if sum(numbers) == target:
            answer += 1
        return

    numbers[depth] *= 1  # 해당 숫자를 더하는 경우
    dfs(numbers, target, depth + 1)
    
    numbers[depth] *= -1  # 해당 숫자를 빼는 경우
    dfs(numbers, target, depth + 1)

    
def solution(numbers, target):
    global N, visited
    N = len(numbers)
    visited = [0] * N
    
    dfs(numbers, target, 0)
    
    return answer