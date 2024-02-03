
from collections import Counter
def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players

