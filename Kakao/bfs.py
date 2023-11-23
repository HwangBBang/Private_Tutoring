# from collections import deque

# arr = deque([1, 2, 3, 4, 5, 6, 7])

# print(arr)

# arr.appendleft(8)
# print(arr)

# arr.append(8)
# print(arr)

# arr.remove(8)
# print(arr)

# arr.rotate(1)
# print(arr)

# arr.rotate(1)
# print(arr)

# arr.rotate(-1)
# print(arr)

# s = 'abcdefg'
# arr.extend(s)

# print(arr)

# arr.clear()
# print(arr)

from collections import deque


# bfs 의 핵심은 방문한 노드를 기록하는것이다.

# 1. 시작 노드를 대기열(큐) 에 삽입 .


i_d = [0, 1, 0, -1]
j_d = [1, 0, -1, 0]
# visited [True, False ,True ...]  방문 기록을 다음 처럼 관리
#


def bfs(graph, s_i, s_j, visited):
    que = deque(graph[s_i][s_j])
    visited[s_i][s_j] = True
    while que:
        # 탐색
        # 가장 먼저 들어간 놈 빼기
        que.popleft()
        # 인접 노드 체크
        for i, j in zip(i_d, j_d):
            if not visited[s_i+i][s_j+j]:
                que.append(graph[s_i+i][s_j+j])


bfs(graph=["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    s_i=0,
    s_j=0,
    visited=[[[0 for _ in range(5)]] for _ in range(5)])
