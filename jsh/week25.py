# # n = int(input())

# # # # 오름차순 -> 오름차순 좋아
# # # for i in range(0, n, 1):  # i = 0 ,i = 2(n=3)
# # #     for k in range(n-i-1):
# # #         print(' ', end=" ")
# # #     for j in range(2*(i)+1):
# # #         print('@', end=" ")
# # #     print()

# # # # 내림차순 -> 내림차순 좋아
# # # for i in range(n-1, 0, -1):
# # #     for k in range(n-i): # 오름
# # #         print(' ', end=" ")
# # #     for j in range(2*(i)-1): #내림
# # #         print('@', end=" ")
# # #     print()


# # # for i in range(1, n+1, 1):  # 세로 : 행
# # #     if i % 2:
# # #         print("*", end=" ")
# # #     else:
# # #         for j in range(i):  # 가로 : 열
# # #             print("*", end=" ")
# # #     print()


# # #  홀수 일때 ,  오름차순 +1
# # #  짝수 일때 ,  내림차순 -1

# # for i in range(1, 2*n+1, 1):  # 세로 : 행
# #     if i % 2 == 1:  # 홀수
# #         for j in range((i//2)+1):
# #             print("*", end=" ")
# #     if i % 2 == 0:          # 짝수  i==2
# #         for k in range((n+1) - i//2):  # 가로 : 열
# #             print("*", end=" ")
# #     print()


# # # *         i = 1 -> 0 + 1
# # # * *       i = 3 -> 1 + 1
# # # * * *     i = 5 -> 2 + 1
# # # * * * *   i = 7 -> 3 + 1
# # # * * * * * i = 9 -> 4 + 1


# # # 짝수
# # # * * * * * i = 2 ,1  -> 5개
# # # * * * *   i = 4 ,2 -> 4개
# # # * * *     i = 6 ,3 -> 3개
# # # * *       i = 8 ,4  -> 2개
# # # *         i = 10 ,5 -> 1개


# arr = [
#     [1, 2, 3, 4],
#     [2, 1, 4, 3],
#     [3, 4, 1, 4],
#     [3, 4, 4, 1]
# ]

# # for i, line in enumerate(arr):
# #     for j, node in enumerate(line):
# #         if node == 4:
# #             arr[i][j] = 0

# # for i in range(len(arr)):
# #     for j in range(len(arr[i])):
# #         if arr[i][j] == 4:
# #             arr[i][j] = 0

# # for line in arr:
# #     for node in line:
# #         print(node, end=" ")
# #     print()
# n, k = map(int, input().split())

# arr = [0]*n  # 세로
# [0,0,0,0]
# arr[0] = list(map(int, input().split()))
# [[1, 2, 3, 4],0,0,0]

# arr[1] = list(map(int, input().split()))
# [[1, 2, 3, 4],[2, 1, 4, 3],0,0]

# arr[2] = list(map(int, input().split()))
# [[1, 2, 3, 4],[2, 1, 4, 3],[3, 4, 1, 0],0]

# arr[3] = list(map(int, input().split()))
# [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 0], [3, 4, 4, 1]]
# for i in range(n):
#     arr[i] = list(map(int, input().split()))

# print(arr)


# n = 4

# for i in range(n):
#     for j in range(n, 0, -1):
#         print(j, end=" ")
#     print()


arr = [
    [1, 2, 3, 4],
    [2, 1, 4, 3],
    [3, 4, 1, 0],
    [3, 4, 4, 1]
]

print(arr[3][2])
