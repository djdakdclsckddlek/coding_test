from collections import deque
def solution(priorities, location):
    prior = deque(priorities)
    count = [i for i in range(len(priorities))]
    while 1:
        if prior[0] != max(prior):
            prior.append(prior.popleft())
            count.append(count.pop(0))

        else:
            prior.popleft()
            if count.pop(0) == location:
                return len(priorities) - len(count)
        