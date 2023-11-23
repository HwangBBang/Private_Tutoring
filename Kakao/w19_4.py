def solution(stones, k):
    answer = 0
    
    while cross(stones,k):
        print(answer)
        answer += 1
    
    return answer

def cross(stones,k):
    k_cnt = 0
    for i,v in enumerate(stones):
        if k < k_cnt :
            return False
        if v == 0: 
            k_cnt += 1 
            continue
        else:
            v -= 1 
            stones[i] = v
            
solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)