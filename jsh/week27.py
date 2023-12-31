
# # for i in range(1, n+1):
# #     for _ in range(i):
# #         print("*", end="")
# #     print()
# #     for _ in range(n - i + 1):
# #         print('*', end="")
# #     print()

# # 오름차순과 내림차순
# # * 24
# # **** 28

# # ** 24
# # *** 28

# # *** 24
# # ** 28

# # **** 24
# # * 28

# for i in range(1, n+1):
#     for _ in range(i):
#         print("*", end="")
#     print()

#     for _ in range(n-i+1):
#         print("*", end="")
#     print()
# 2*n -> 홀 or 짝
# n -> 홀 + 짝


# for i in range(1, 2*n+1):
#     if i % 2:
#         for _ in range((i+1)//2):
#             print("*", end="")
#         print()
#     else:
#         for _ in range(n+1 - (i)//2):
#             print("*", end="")
#         print()

# 1 3 5 7 홀수 - 오름
# 1 2 3 4

# 2*x -1 = y
# (y + 1) // 2 =  x

# 2 4 6 8 짝수 - 내림 / n = 4
# 4 3 2 1

# 2 4 6 8 10 짝수 - 내림 / n = 5
# 5 4 3 2 1

# 2 4 6 8 10 12 짝수 - 내림 / n = 6
# 6 5 4 3 2 1

# n - i//2
# 6+1 - 2//2 = 6
# 6+1 - 4//2 = 5
# n+1 - i//2

# n  = 1
# n = int(input())
# for i in range(2*n+1):
#     for j in range(2*n+1):
#         if i % 2 == 1 and j % 2 == 1:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")

# if i % 2 == 1 and j % 2 == 1:
#     print(" ", end=" ")
# else:
#     print("*", end=" ")
# print()

#   0 1 2 3 4
# 0 * * * * *
# 1 *   *   *
# 2 * * * * *
# 3 *   *   *
# 4 * * * * *

# 1,1, 1,3 ,3,1, 3,3

# 최초 모습은 정사각형이네 ~
# 어떤 기준으로 변형한거지 ?
# 기준을 찾으면 내가 제어해 ~

n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i != 0 and j % 2 == 0:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()


for i in range(1, n+1):
    for j in range(1, n+1):
        if j % 2 == 1:
            if i == 1:
                print('*', end=" ")
            else:
                print(' ', end=" ")
        else:
            if i <= j:
                print('*', end=" ")
            else:
                print(' ', end=" ")
    print()

#   1 2 3 4 5 6
# 1 * * * * * *
# 2   *   *   *
# 3   *   *   *
# 4   *   *   *
# 5   *   *   *
# 6   *   *   *


#   1 2 3 4 5 6
# 1 * * * * * *
# 2   *   *   *
# 3       *   *
# 4       *   *
# 5           *
# 6           *
