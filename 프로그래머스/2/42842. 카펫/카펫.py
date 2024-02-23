def solution(brown, yellow):
    # 최소 너비
    w, h = 3, 3
    yel, bro = 0, 0
    while 1:
        yel = (w-2) * (h-2)
        bro = (w*h) - yel
        
        if bro == brown and yel == yellow:
            return [w, h]
        elif yellow > yel and bro == brown:
            w -= 1
            h += 1
        else:
            w += 1
