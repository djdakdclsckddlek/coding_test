def solution(m, n, puddles):

    map = [[1] * m for _ in range(n)]
    denominator = 1000000007

    # 왼쪽 끝,위 끝에 장애물 있는 경우 0으로 바꾸기
    for x, y in puddles:
        if x == 1:
            for i in range(y-1, n):
                map[i][x-1] = 0
        if y == 1:
            for i in range(x-1, m):
                map[y-1][i] = 0

    # 우물 0으로 채워넣기
    for x, y in puddles:
        map[y-1][x-1] = 0

    for x in range(m):
        for y in range(n):
            # 범위 벗어나는 경우
            if x-1 < 0 or y-1 < 0:
                continue
            # 우물인곳 벗어나기
            if map[y][x] == 0:
                continue
            # 왼쪽 체크, 위 체크
            map[y][x] = map[y][x-1] + map[y-1][x]

    return map[n-1][m-1] % denominator