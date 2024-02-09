# 카펫

def solution(brown, yellow):
    w, h = 3, 3
    
    while True:
        yel = (w-2) * (h-2)
        bro = w*h - yel
        
        if yellow == yel and bro == brown:
            return [w, h]
        
        if yellow > yel and bro == brown:
            w -= 1
            h += 1
        else:
            w += 1