 
# 4,3,1,1,3,2,4
# def check_temp():
#     cnt ,i = 0, 0
#     while True:
#         # 인접한 노드의 값이 모두 다를 때 
#         if i+1 == len(temp):
#             break
#         # 이웃한 노드간 값이 같다면 둘다 pop , 앞에서부터 다시 시작
#         if temp[i] == temp[i+1]:
#             print(f'i is {i} pre {temp}')
#             temp.pop(i)   # del temp[i];
#             temp.pop(i) # del temp[i+1];
#             print(f'i is {i} after {temp}')
#             i = 0
#             cnt += 2
#         i+=1
#     return cnt 

def solution(board, moves):
    stack = [0]
    answer,cnt = 0,0
    moves = [move - 1 for move in moves]
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move] != 0: 
                stack.append(board[i][move]) 
                
                board[i][move] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt += 2    
                break
    answer = cnt
    return answer

print(solution(board=[[0,0,0,0,0],
                      [0,0,1,0,3],
                      [0,2,5,0,1],
                      [4,2,4,4,2],
                      [3,5,1,3,1]
                     ]
         ,moves=[1,5,3,5,1,2,1,4]))


# [
#     [0,0,0,0,0],
#     [0,0,1,0,3],
#     [0,2,5,0,1],
#     [4,2,4,4,2],
#     [3,5,1,3,1]
# ]
# [1,5,3,5,1,2,1,4]
# for select in move:
#   for i in (행의 크기 )
#       if board[i][select] != 0: 
#           temp.append(board[i][select])  # temp 는 stack 
#           board[i][select] = 0
#   check_temp() check_temp 에 인접한 요소가 있다면 pop 
