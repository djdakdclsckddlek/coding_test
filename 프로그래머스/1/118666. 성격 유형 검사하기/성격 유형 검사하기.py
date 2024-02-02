def solution(survey, choices):
    mbti = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0, }
    # 설문 안에서 돌아가면서 선택지 점수 +
    for i in range(len(survey)):
        option1, option2 = survey[i][0], survey[i][1]
        choice = choices[i]
        
        if choice == 4:
            continue
        elif 1 <= choice <= 3:
            mbti[option1] += 4 - choice
        elif 4 <= choice <= 7:
            mbti[option2] += choice - 4
        
    mbti1 = max(["R", "T"], key=lambda x: mbti[x])
    mbti2 = max(["C", "F"], key=lambda x: mbti[x])
    mbti3 = max(["J", "M"], key=lambda x: mbti[x])
    mbti4 = max(["A", "N"], key=lambda x: mbti[x])
   
    return mbti1 + mbti2 + mbti3 + mbti4 