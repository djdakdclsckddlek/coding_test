from collections import Counter

def solution(topping):
    answer = 0
    
    # a가 토핑을 b에게 주면서 토핑의 개수가 같은경우 리턴
    # 딕셔너리활용
    
    aa = Counter(topping)
    bb = set()
    
    for top in topping:
        # a가 b에게 토핑을 한개씩 주기
        aa[top] -= 1
        bb.add(top)
        
        # a에게 남은 토핑이 없다면 지워주기
        if aa[top] == 0:
            aa.pop(top)
        
        if len(aa) == len(bb):
            answer += 1
    
    return answer