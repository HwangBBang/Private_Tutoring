# 출력..
# print() 함수
# 터미널에 출력하는 함수
# end = "\n" , sep = " "
# sep , 여러개의 인자를 구분하는 아이.

# print(1, 2, 3+2, sep="바보")

# input() 함수
# 터미널로 입력받는 함수
# map() , split()
# 입력받는 인자들을 구분,,


# 연산..
# + - * /(진짜나누기) //(몫나누기) %(나머지나누기) **(승수)

# 자료형 type
# 연산 규칙을 규정하기위해.
# int : 정수 , str : 문자열 , float : 실수 , bool : 참,거짓

# str +연산
# print('1'+'3')  # 13
# 문자열 : 문자 + 문자 / 문자들이 나열(더해서) 되어있다.

# int +연산
# print(1 + 3)  # 4

# input() 의 기본 자료형 str
# 형변환..
# a = int("2")  # 더이상 str 아니야! -> int 야
# print(type(a))
# a = float("2")  # 더이상 str 아니야! -> float 야
# print(type(a))


# if문 / 분기문
# 블럭 단위 개념을 이해하자~

# if - else , if - elif , if - elif - else

# if | if 다른 블럭이다.

# if False:
#     print("play : if")
# else:
#     print("play : else ")


# for 문, while 문 / 반복문
# 블럭단위
# for 문은 ? : 범위를 알거나 정도(횟수)를 알때
# while 문은 ? :  범위를 모르거나 정도(횟수)를 모를때

# for i in range(횟수):
# for i in range(시작, 종료포인트, (1)):
# for i in range(시작포인트, 종료포인트, 종료에 도달하는 방법):
# i 반복문 임시 변수가 활용 되지않을 때  i -> _


# while condition:
#   실행중~
#   실행중~
#   실행중~
#   실행중~
#   condition = False

# break , continue
# break : 반복문을 깨 부셔요
# continue : 아래를 다 건너뛰고 조건을 확인하러가~


# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("|", end=" ")
#     print()
# for i in range(5):
#     for j in range(5-i):
#         print("|", end=" ")
#     print()


# n 개를 입력받아줘
# n = int(input())
# for _ in range(n):
#     a= int(input())
#     if a%3==0 and a%2==1:
#         print(a)
