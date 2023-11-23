def solution(answers):
    answer = []
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    assert cnt_1 > 0
    
    per1 = list(range(1,6))*2000
    per2 = [ 2, 1, 2, 3, 2, 4, 2, 5]*1250
    per3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
    for idx,ans in enumerate(answers):
        if ans == per1[idx]:
            cnt_1 += 1
        if ans == per2[idx]:
            cnt_2 += 1
        if ans == per3[idx]:
            cnt_3 += 1
    
    if max(cnt_1,cnt_2,cnt_3) == cnt_1:
        answer.append(1)
    if max(cnt_1,cnt_2,cnt_3) == cnt_2:
        answer.append(2)
    if max(cnt_1,cnt_2,cnt_3) == cnt_3:
        answer.append(3)
    # print(answer)
    return answer

solution([1,3,2,4,2])