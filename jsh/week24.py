# # 세로 -> 가로

# # 줄어드는 형태 (내림차순)
# for i in range(5):  # 세로
#     for j in range(5-i):  # 가로
#         print("*", end="")
#     print()

# # 늘어나는 형태 (오름차순)
# for i in range(1, 6):  # 세로
#     for j in range(i):  # 가로
#         print("*", end="")
#     print()

# # 가로가 바뀌는 방법이 달라지면, 다른 for 문 써야해


# n = int(input())

# for i in range(0, n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()
# for i in range(2, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # i = 0
# * * * *
# # i = 1
# * * *
# # i = 2
# * *
# # i = 3
# *
# # i = 4
#
# # i = 2
# * *
# # i = 3
# * * *
# # i = 4
# * * * *


# n = 2
# * * *

# n = 3
# * * * * *

# n = 5
# * * * * * * * * *

n = int(input())
# ****** 3 0 3
# **  ** 2 2 2
# *    * 1 4 1
for i in range(n):
    for j in range(n-i):  # 별표
        print('*', end="")
    for k in range(i*2):  # 공백
        print(' ', end="")
    for j in range(n-i):  # 별표
        print('*', end="")
    print()
# ***
# **
# *


# k가 어떤 수 던상 관 없어

# 2*k -1 ,2*k +1
# 2k

# ㅁ ㅁ *
# ㅁ * * *
# * * * * *
