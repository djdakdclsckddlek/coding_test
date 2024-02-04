def solution(id_list, report, k):
    
    #사용자 아이디, 사용자 신고한아이디, 정지기준횟수
    # 각 회원당 받게되는 정지성공 메일 개수
    result = []
    id_dict = {i: 0 for i in id_list}
    report_count = {i: 0 for i in id_list}
    reporter_dict = {i: set() for i in id_list}
    
    for po in report:
        id1, id2 = po.split()
        if id1 not in reporter_dict[id2]:
            id_dict[id2] += 1
        
        reporter_dict[id2].add(id1)
    
    for i in id_dict:
        if id_dict[i] >= k:
            for reporter in reporter_dict[i]:
                report_count[reporter] += 1
    
    for count in report_count.values():
        result.append(count)
    
    print(id_dict, report_count)
    return result