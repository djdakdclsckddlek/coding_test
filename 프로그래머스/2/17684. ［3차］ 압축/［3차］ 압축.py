def solution(msg):
    msgdict= {chr(64+i): i for i in range(1, 27)}
    idxnum = 26
    
    word = ''
    answer = [0]
    for i in range(len(msg)):
        word += msg[i]
        
        if not word in msgdict:
            idxnum += 1
            msgdict[word] = idxnum
            
            # 사전에 없으면 사전에 추가 후 word를 msg[i]로 초기화
            word = msg[i]
            answer.append(msgdict[word])
        else:
            # 사전에 있으면 answer에 마지막 숫자를 변경
            answer[-1] = msgdict[word]
    return answer