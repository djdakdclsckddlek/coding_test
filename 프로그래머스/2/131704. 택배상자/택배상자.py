def solution(order):

    stack = []
    index = 0
    for num in range(1, len(order) + 1):
        # 더하고
        stack.append(num)
        # 더할때마다 체크하기
        while stack and stack[-1] == order[index]:
            stack.pop()
            index += 1

    return index