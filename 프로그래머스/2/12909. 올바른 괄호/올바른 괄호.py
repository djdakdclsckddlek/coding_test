def solution(s):
    answer = []
    for w in s:
        if w == '(':
            answer.append(w)
        elif w == ')' and answer:
            answer.pop()
        else:
            return False
    return True if len(answer) == 0 else False