def solution(data, ext, val_ext, sort_by):
    #data 코드번호 제조일 최대수량 현재수량
    # 데이터를 ext기준으로 val_ext보다 작은 데이터 중에 sort_by순으로 정렬하기
    options = ["code", "date", "maximum", "remain"]
    
    data = list(filter(lambda x: x[options.index(ext)] < val_ext, sorted(data, key = lambda x: x[options.index(ext)])))
    
    return sorted(data, key=lambda x:x[options.index(sort_by)])
