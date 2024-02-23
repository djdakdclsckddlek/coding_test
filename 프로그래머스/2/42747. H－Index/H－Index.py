def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return i
    return len(citations)


# def solution(citations):
#     answer = 0
#     citations.sort(reverse=True)
#     n=len(citations)
#     for i in range(n):
#         if citations[i]<i+1:
#             return i

#     return n