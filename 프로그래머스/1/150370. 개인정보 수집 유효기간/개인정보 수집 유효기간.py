def solution(today, terms, privacies):
    result = []
    deadline = {}
    today = list(map(int, today.split('.')))
    
    for i in terms:
        key, val = i.split(' ')
        deadline[key] = int(val)
    
    for i, privaci in enumerate(privacies):
        date, line = privaci.split(' ')
        date = list(map(int, date.split('.')))
        
        month = today[1] - date[1]
        
        if today[0] > date[0]:
            month += 12 * (today[0] - date[0])
        if today[2] >= date[2]:
            month += 1

        if deadline[line] < month:
            result.append(i+1)
    
    return result