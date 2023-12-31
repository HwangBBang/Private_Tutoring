# ~~ !!사고!! ~~ 프로그래밍 언어 <- 활용(도구)

# 조건 (분기)문

# 문제.. -> 정의 !
# 홀수의 정의 -> 2로나누었을 떄 나머지가 1인 녀석
# 7의배수 -> 7로 나누었을 때 나머지 0인녀석
# 369당첨수 -> 3,6,9를 포함한 녀석. (100 미만)
# -> %10 = 3,6,9 (1의 자리수가 369 인 녀석)
# -> //10 = 3,6,9 (2의 자리수가 369 인 녀석)

# 1
# 2
# "3"
# 4
# 5
# "6"
# 7
# 8
# "9"
# 10
# 11
# 12
# "13"
# 14
# 15
# "16"
# ...
# "30"
# "31"
# "32"

# 짝수 -> "?" -> 2로 나누었을 때 나머지가 0인 녀석  %2==0

# if - elif - else
# 블럭 단위로 프로그래밍
# and or not [bool]
##################
# if A and B :

# if A
#   if B :
####################################
# if A :
#    -> A[T] B[?] C[?]
#   if B :
#       -> A[T] B[T] C[?]
#     if C :
#         -> A[T] B[T] C[T]
#     else :
#         -> A[T] B[T] C[F]
#   else :
#       -> A[T] B[F] C[?]
# else :
#    -> A[F] B[?] C[?]
####################################
# 8 가지
# TTT
# TTF
# TFT
# TFF
# FTT
# FTF
# FFT
# FFF
####################################
# if A or B or C :
#   -> TTT
#   -> TTF
#   -> TFT
#   -> TFF
#   -> FTT
#   -> FTF
#   -> FFT
# else :
#   -> FFF

####################################
# 반복문 .
# for -> 반복하는 정도(횟수)를 알때
# for i in range ():

# while -> 반복하는 정도(횟수)를 모를때
# while ():
####################################
# break -> "즉시" 깨 부 시 다!
# continue -> "즉시" (밑으로 안 내려감) 다음 회차로가렴~ (조건 확인)

# for <-> while + cnt ,if

# for _ in range(5):
#     print(1)

# cnt = 0
# while 1:
#     if cnt >= 5:
#         break
#     print(2)
#     cnt += 1
# float__________.____________16____________|
# int ________________________________
# a = 3/5
# print("%.16f" % a)
# for i in range(1,40+1):
#     if not (i%2==0 and i%4!=0):
#         if not((i//8)%2==0):
#             if not(i%7<4):
#                 print(i,end=" ")


5

# 1 2 3 4 5
# res 1
# res 3
# res 6 -> break -> i 값. ->

# n = int(input())
# res = 0
# for i in range (1,101):
#     if res >= n:
#         print(i-1)
#         break
#     res += i


# 홀 -> X
# 짝 -> //2

# 8  짝
# 6  짝
# 3  홀
# 20 짝

# cnt = 0
# while 1:
#     n = int(input())

#     if n % 2 == 0:

#         n = n//2
#         print(n)
#         cnt += 1
#     else:
#         continue

#     if cnt >= 3:
#         break

# 계속 돌아가
# 입력
# 체크해 (카운트 올려)
# 끝나냐?


# 코드 솔루션
# while
#
#   if : break

# import !


# 1 / 7
#          0.
# 1 / 7 = 1 | 3
# 30 / 7 = 4 | 2
# 20 / 7 = 2 | 6
# 60 / 7 = 8 | 4

# a, b = 1, 7
# a %= b  # 3..
# print(f"{a//b}.", end="")
# for _ in range(20):
#     a *= 10
#     print(a//b, end="")
#     a %= b


a, b = 2, 13

# i = a
# while i <= b:
#     print(i, end=" ")
#     if i % 2 == 1:
#         i *= 2
#     else:
#         i += 3

# a ------> b
# for i in range(a, b+1, 1):
#     if b >= a:
#         print(a, end=" ")
#         if i % 2 == 1:
#             a *= 2
#         else:
#             a += 3
