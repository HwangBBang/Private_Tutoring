# # 제어 (if)
# # -> 홀수?
# # -> 4배수니?
# # -> 홀수 and 4배수니?
# # -> 홀수 and 4배수니? 100 의 배수가 아니니?


# # 논리적인 생각 . -> 경우의 수 + 배타적인 사고 . ( 이분법 적으로 )

# # 남자 + 여자

# # 3 개 -> a,b,c -> a,b,c

# # 5 이하 일때 ->  $$$
# # 5 초과 일때 ->  $$$

# #  5 이하 인지 if -> else
# #
# # 가장 밖의(큰 부분을) 컨트롤한다.
# #
# #

# # if A and B and C and D :

# if A:
#   if B:
#       if C:
#           if D:
#  -> A,B,C,D
#  else:
#  -> A,B,C,~D
# # else:
# # if D:
# # -> A,B,~C,D
# # else:
# # -> A,B,~C,~D
# # else:
# # @@@@
# # else:
# # @@@@
# # else:
# # @@@@


# # if else elif

#  변수 vs " " (문자열)
#  W   vs  "W"

# # print (.. ,sep=" ",end = "\n")

# # def print(args* , sep, end):
# #     sep = ?
# #     end = ?
# #
# #
# # input().split(" ")
# # map(int ,input().split())

# # -> int, str
# # 한줄에 여러개 받아? -> map
# # map 을 쓸 때 자료형을 입력해줘야하는데 하나밖에 못하잖아?

# # a,b = map(str ,input().split())
# #   -> a = int(a)

# # a,b = map(int ,input().split())
# #    -> b = str(b)


# # 번호를 입력하면
# #   -> 필요해
# a = 111
# # 해당하는 학생의 이름을 출력하는 프로그램을 작성하세요.

# # 1번은 John, # 2번은 Tom, # 3번은 Paul입니다. # 이외 Vacancy.
# if a == 1:
#     print("John")
# elif a == 2:
#     print("Tom")
# elif a == 3:
#     print("Paul")
# else:
#     print("Vacancy")

# # 두 개의 정수 a, b를 입력받아
# # a가 b보다 크다면 두 수의 곱을 출력하고,
# # 그렇지 않다면 b를 a로 나눈 몫을 출력하는 프로그램을 작성해보세요.

# a, b = map(int, input().split())

# if a > b:
#     res = a*b
# else:
#     res = b//a
# print(res)


# # 정수 a를 입력받았을 때
# # a의 값이 5인 경우엔 A한다.
# # 이후
# # 2의 배수인 경우에 B
# # 둘 다 해당하지 않는 경우에는 아무 값도 출력하지 않습니다.


# # 2개의 정수를 입력 받아
# a, b = map(int, input().split())

# if a < b:
#     print(1)
# else:
#     print(0)

# if a == b:
#     print(1)
# else:
#     print(0)

# # 첫 번째 수가 더 작으면 1 ,
# # 아니면 0을 출력하고,

# # 두 개의 수가 같으면 1 ,
# # 아니면 0 을 출력하는


# 3개의 정수를 입력 받아
a, b, c = map(int, input(). split())
# 첫 번째 수가 세 정수의 최솟값과 일치한다면 1
# a < b < c
# a < c < b
# if a <= b and a <= c:


# 3개의 정수를 입력받아
# 입력받은 수 중 최솟값을 출력
