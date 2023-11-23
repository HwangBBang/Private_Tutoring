# if  a : a이라면 아래블럭을 수행시켜

# elif b : if 가 아니고  b 이거라면 나의 아래블럭을 수행시켜

# else  : if 가 아니라면 나의 아래블럭을 수행시켜

# 논리 연산자
# and , or , not

# 키도 크고싶고 공부잘하고싶어
# 키크다 and 공부잘한다.

# 키도 크거나 공부잘하고싶어 (둘중하나만 되어도 좋아)
# 키크다 or 공부잘한다.

# 키가 작고싶어
# not 키크다

# 부울 연산
# True , False 들의 조합들이 어떤결과가 나오는지??!
# 진리표

# |  A  | and |  B  |  결과
#    0           0      0
#    0           1      0
#    1           0      0
#    1           1      1

# |  A  | or |  B  |  결과
#    0           0      0
#    0           1      1
#    1           0      1
#    1           1      1

#         not |  A  |  결과
#                0      1
#                1      0

# 침대에 누음
import math    # import 가져오는거야! math 라는 책을
import random  # import 가져오는거야! random 이라는 책을

#           0  ,    1   ,   2 (번째)
states = ["편해", "그냥뭐~", "안편해"]
# states2 = ("편해", "그냥뭐~", "안편해")

states[1] = "난 딴 침대가 더 좋아"
# states2[1] = "아 어쩔수없이 잔다 "


# i = int(random.random()*3)
# # 랜덤 쓸일 많아 컴퓨터가 표현할 수 있는 수는 정해져있어. -> 효율성!
# # random 함수 다 똑같이 처리해  . 어떻게요 !?!

# # 0~3 실수 float
# # 0,2.99999999999999999 절대로 3은 안돼

# # for _ in range(100):
# #     num = random.random()*3
# #     print(num)
# #     print("%.f" % num)

# state = states[i]

# # 침대 누었을 때 , 편한지 안편한지를 구분
# if state == "편해":
#     print("침대 좋아 !")
# elif state == "안편해":
#     print("침대 싫어 !")
# else:
#     print("그냥 뭐~ 쓸만하네!")


# # print(math.pi)
a, b = 3, 3

# if a <= b:
#     print(1)
# else:
#     print(0)
# print(1) if a <= b else print(0)

# if a != b:
#     print(1)
# else:
#     print(0)
# print(1) if a != b else print(0)


# if - else ( elif )

# and , or

# == , <, > , <= ,>=


# 블럭단위 코딩

# 산술 연산자

# + - * / // % **
#  a = a+1
# a += 1
# a -= 1

# 제곱은 그숫자 곱하기 그숫자

# 1의제곱은 ? 1*1 = 1

# 6의제곱은 ? 6*6 = 36

# -7의 제곱은? -7*-7 = 49

# -3 의 제곱은? -3*-3 = 9

# 세제곱은 ?
# 그숫자 곱하기 그숫자 곱하기 그 숫자

# 2의 세제곱 = 2**3 = 8
# -2의 세제곱 = -2 * -2 * -2 =  ---8

# 시훈이가 음수의 곱셈을 못해
# 왜 못할까  잘못 생각하고있어

# -2*-3 = 6
# -       -> -
# -,-     -> +
# -,-,-   -> -
# -,-,-,- -> +

# 첫 번째 줄
# A의 수학 , A의 영어
mathA, EngA = map(int, input().split())
# B의 수학 , B의 영어
mathB, EngB = map(int, input().split())

re = float(input())
re(float, input())


# 멀티 스레드 .,
