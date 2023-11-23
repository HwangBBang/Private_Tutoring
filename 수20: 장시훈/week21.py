# # # nest : 둥지
# # # nested : 중첩된

# # # nested if
# # # if
# # #     if

# # # nested for

# # # for i in range(5):  # 세로
# # #     for j in range(5-i):  # 가로
# # #         print('*', end="")
# # #     print()  # 왜 쓴거에요?


# # # for i in range(5):  # 세로
# # #     for j in range(4-i):  # 가로
# # #         print(' ', end="")
# # #     for j in range(i+1):  # 가로
# # #         print('*', end="")
# # #     print()

# # # for i in range(5):  # 세로
# # #     for j in range(i+1):  # 가로
# # #         print('*', end="")
# # #     print()
# # # i :0 ~ 4
# # # i = 0 -> *
# # # i = 1 -> **
# # # i = 2 -> ***

# # # for j in range(4):
# # #     print(j, sep="", end=" ")
# # # print()
# # # for j in range(4):
# # #     print(j, sep="", end=" ")
# # # print()
# # # for j in range(4):
# # #     print(j, sep="", end=" ")
# # # print()
# # # for j in range(4):
# # #     print(j, sep="", end=" ")
# # # print()


# # # end=""

# # flag = 1  # true 모든 수 3의 배수이다.
# # #          false 모든 수 3의 배수가 아니다.
# # for _ in range(5):
# #     a = int(input())
# #     if a % 3 != 0:  # a가 3의 배수가 아니다.
# #         flag = 0

# # print(flag)

# # iteration : 반복
# # iterate : 반복하다

# # i = 5
# # * * * * * j = 5
# # * * * * * j = 5
# # * * * * * j = 5
# # * * * * * j = 5
# # * * * * * j = 5

# # i = 5
# # * * * * * j = 5
# # * * * *   j = 4
# # * * *     j = 3
# # * *       j = 2
# # *         j = 1

# n = int(input())
# for i in range(n):
#     if i == 3:
#         continue
#     for j in range(i+1):
#         print(end=" ")
#     print()


# *         i=0
# * *       i=1
# * * *     i=2           i=3
# * * * * * i=4
def solution(strings, n):
    strings.sort(key=lambda x: x[n:])
    answer = strings
    # print(answer)
    return answer


solution(strings=["sun", "bed", "car"], n=1)
