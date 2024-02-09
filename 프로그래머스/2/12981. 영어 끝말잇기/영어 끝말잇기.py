
def solution(n, words):
    words_set = set()
    words_set.add(words[0])
    
    for i in range(1, len(words)):
        if (words[i] in words_set) or (words[i-1][-1] != words[i][0]):
            return [(i%n)+1, (i//n) +1]
        
        words_set.add(words[i])
    
    return [0,0]