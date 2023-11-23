# n = int(input())
# cnt = 0

# # 윤년 !
# for i in range(1, n+1, 1):
#     if i % 4 == 0:
#         if i % 100 == 0 and i % 400 != 0:  # 평년 (특이)
#             continue
#         else:  # 윤년 (디폴트)
#             cnt += 1
#     else:  # 평년
#         continue
# print(cnt)


# #
# 1 2 3 4 5 6 7 8 .. k .. -> for 반복문
# 2 3 5 7 -> 소수라는 걸 어떻게 판단할꺼야 ?
# 소수는 뭔데? -> 1과 나만 약수로 갖는 아이야.
# 이게 소수인지 궁금한 수?

# for j in range(2,이게 소수인지 궁금한 수):
#   if 이게 소수인지 궁금한 수%j==0:
#       소수 아니네. flag = False
#   if flag == True:


# 마름모 .

# n = int(input())

# cnt = 0
# for i in range(2, n+1):
#     for j in range(1, i+1):
#         if i % j == 0:
#             cnt += 1
#     if cnt == 2:
#         print(i, end=" ")
#     cnt = 0


# for i in range(0,10): # 10
#     for j in range(0,10): # 10
