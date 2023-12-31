

# 이중 반복문( 중첩 반복문 )

# for
# 어떤 범위(규칙 횟수 정도)
# for 반복 : 1차원 반복 .
# -------------------->
# for-for 반복 : 2차원 반복 .
# [-]------------------->
# [|]
# [|]
# [|]
# [|]
# [|]
# -[-]------------------>
#  [|]
#  [|]
#  [|]
#  [|]
#  [|]
# --[-]----------------->
#   [|]
#   [|]
#   [|]
#   [|]
#   [|]

# for i in range(10):  # 1차원 반복
#     print("-", end="")

# for i in range(5):  # 1차원 반복
#     for j in range(i+1):  # 1차원 반복
#         print("*", end="")
#     print()


# # 밖의 for을 기준을 잡고 생각해라 .

# for i in range(5):  # 1차원 반복
#     for k in range(5-i):  # 1차원 반복
#         print("*", end="")
#     print()


# # # # while


n = int(input())
# for i in range(n):
for i in range(n, 0, -1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()

# A B C
#   D

# EFGHIJKLMNOPQRSTUXYZABC

# n 내림차순,,
# 여지껏, 오름차순
# 밖 -> 세로 n 번만..


# n = 3
# 2n + 1 2n -1
# 5 -> 3 -> 1

# n = 2

# 3 -> 1


# *****
#  ***
#   *
#  ***
#   *

# 3 5 7 9
# i == 1, j == 1
# i == 2, j == 3
for i in range(2, n+1):
    for j in range(2*i-1):
        pass
