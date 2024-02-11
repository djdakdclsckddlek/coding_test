def solution(genres, players):
    gen_dict = {}
    playlist = {}
    result = []
    for i in range(len(genres)):
        if genres[i] not in gen_dict:
            gen_dict[genres[i]] = players[i]
            playlist[genres[i]] = [[i,players[i]]]
        else:
            gen_dict[genres[i]] += players[i]
            playlist[genres[i]].append([i,players[i]])
    
    for gen in sorted(gen_dict.keys(), key=lambda x: gen_dict[x], reverse= True):
        playnum = 0
        for player in sorted(playlist[gen], key=lambda x:x[1], reverse=True):
            if playnum >= 2:
                break
            result.append(player[0])
            playnum += 1
            
    return result