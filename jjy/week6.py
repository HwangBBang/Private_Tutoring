# 변수
# 초기화
# 자료형

# a = 13 : 초기화

# int a = 13; # 선언
# a = 12; # 초기화

a = 13  # 파이썬에서는 선언과 초기화 가 동시에 ,

# 자료형
# 자료형을 모르고 있으면 실수 많아 ,
# 자료형 | 정수int , 문자"열" str , 실수 float , 부울 bool

# 문자"열" str
# 문자열 : 문자 + 문자 + 문자 + 문자 .... 문자
# 문자열 : 문자열 + 문자열 .... 문자
# 문자열 : 문자열 + 문자열


# (자료)형 변환..
# type 을 변환 .
# "1" , 1

# print("1", 1)  # 1 1
# print("1"+"1", 1+1)  # 11 2

# input() 터미널을 통해서 입력을 받을때, 기본적으로 받는타입이 Str
# 난 숫자를 입력받고 싶은데... 문자열을 입력받잖아 .
# 그래서 형변환을 해줘야해 .

# print(type(int(input())))
# print(type(input()))
# 논리 연산의 flag : True , False
# True : 1  / Flase : 0
# |_______._____________|


# 사칙연산 ,,
# + - *
# /  :  진짜 나누기
# // :  몫 나누기 (정수형을 보장한다.)

# print(3/2)  # 1.5      -> 1
# print(2/3)  # 0.666666 -> 0
# print(3/3)  # 1.0      -> 1

# print(3//2)  # 1.5      -> 1
# print(2//3)  # 0.666666 -> 0
# print(3//3)  # 1.0      -> 1

print(int(3/2))  # 1.5      -> 1
print(int(2/3))  # 0.666666 -> 0
print(int(3/3))  # 1.0      -> 1


# 문자열 내부에 변수를 쓸 수 없어??..


# 리팩토링 ("재활용")
# res = a+b+c
# a, b, c = res, res, res


# input() 함수활용하기..
# print() 함수활용하기..

# 함수 :  기능.!
# 조금은 똑똑한기능들은 옵션? 추가적인 셋을 요구한다 .
# set : 인자(아규먼츠) = 매개변수 (파라미터)
# den -> degree

print("010", "1123", "2131", sep="-")
