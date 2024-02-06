def solution(bandge, health, attacks):
    maxhealth = health
    attacktimes = {k: v for k, v in attacks}
    castingtime = 0
    
    for t in range(1, attacks[-1][0] + 1):
        # 맞을때 생존 >> 체력회복 >> 추가회복(시전시간) >> 최대채력 여부

        if t in attacktimes:
            health -= attacktimes[t]
            castingtime = 0
            if health <= 0:
                return -1
            else:
                continue
        
        health += bandge[1]
        castingtime += 1
    
        if castingtime == bandge[0]:
            health += bandge[2]
            castingtime = 0
        
        if health >= maxhealth:
            health = maxhealth
        
    return health