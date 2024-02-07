from collections import deque as dq
def solution(people, limit):
    people.sort()
    people = dq(people)
    count = 0
    
    while len(people) > 0:
        people1 = people.pop()
        if len(people) > 0 and people[0] + people1 <= limit:
            people.popleft()
        count += 1

    return count