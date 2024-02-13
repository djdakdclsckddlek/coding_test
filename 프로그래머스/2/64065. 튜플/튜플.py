def solution(s):
    n_count = dict()
    s = s.replace('{', '').replace('}', '').split(',')
    
    for i in s:
        i = int(i)
        
        if i not in n_count:
            n_count[i] = 1
        else:
            n_count[i] += 1
            
    return sorted(n_count, key=lambda x: n_count[x], reverse=True)