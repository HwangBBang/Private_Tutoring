from collections import deque


def solution(places):

    answer = []
    for place in places:
        answer.append(check(place))
    print(answer)
    return answer


def check(p):

    for line in enumerate(p):
        for elem in enumerate(line):
            if elem == 'P':  # 시작 P

                return 0  # 거리두기 안지킴

    return 1  # 거리두기 지킴


def bfs():
    visited = [[False for _ in range(5)] for _ in range(5)]
    dis = [[0 for _ in range(5)] for _ in range(5)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    que = deque()
    que.append([line_idx, elem_idx])
    visited[line_idx][elem_idx] = True
    while que:
        que.popleft()
        for i, j in zip(dx, dy):
            if 0 <= line_idx+i and line_idx+i < 5 or 0 <= elem_idx+j and elem_idx+j < 5:
                if not visited[line_idx+i][elem_idx+j]:
                    if p[line_idx+i][elem_idx+j] == 'O':
                        que.append([line_idx+i, elem_idx+j])
                        visited[line_idx+i][elem_idx+j] = True
                        dis[line_idx+i][elem_idx +
                                        j] = dis[line_idx][elem_idx] + 1
                    if p[line_idx+i][elem_idx+j] == 'P' and dis[line_idx][elem_idx] <= 1:
                        return 1


# def isManhaton(p, i, j):
#     for t1 in range(i-2, i+3):
#         for t2 in range(j-2, j+3):
#             if t1 == i or t2 == j or ((t1 < 0) and (t1 > 4)) or ((t2 < 0) and (t2 > 4)):
#                 continue
#             # if p[t1][t2] == 'X':
#             #     continue
#             if p[t1][t2] == 'P' and abs(i-t1)+abs(j-t2) <= 2:
#                 return True

#     return False


solution(places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], [
         "PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])


# 길 이있는지?
# bfs 탐색
# POOPX
# OXPXP
# PXXXO
# OXXXO
# OOOPP
