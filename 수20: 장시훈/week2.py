

# 변수 <- 초기화 (=), 변수 's 자료형(type)

# 변수의 주소의 별명 = 변수의 값

# 변수 's 자료형(type)
# - str ("문자열 시작합니다 , "문자열 끝납니다.)
# - int (정수)
# - float (.이 있으면 )
# - bool (True, False)

# 파이썬의 내장함수 출력과 입력

# print(매개변수) | 함수는 매개변수를 터미널에 출력하는 함수야
# print 옵션 -> 단일 출력, 다중 출력 을 제어 할 수있어
# end = "\n" (newline)
# sep = " " (여러개의 인자들을 출력할 때, 구분하는 아이)

# input() | 함수는 터미널에서 입력을 받아 소스에 전달하는 함수야
# input() 반환하는 자료형 str -> int , float
# 형변환 -> int(input()), float(input())
# 다중출력 -> map() -> map(type , input().split(" "))

# a = bool(input())     # str -> bool
# a = bool(int(input()))  # ste -> int -> bool

# a = bool("0")     # str -> bool
# a = bool(0)  # ste -> int -> bool

# "1313241" -> True
# "-3241" -> True
# "" -> False
# " " -> True
# 0 -> False
# 1,23,31314,-314 -> True
# print(f"{a}  , type is {type(a)}")

# b = " "
# b = bool(b)
# print(f"{b}  , type is {type(b)}")

# 제어문 if - else - elif


# if 1:
#     if 1:
#         pass

# if 1:            #
#     if 1:        #
#         pass     #
# elif 0:          #
#     pass         #
# else:            #
#     pass         #

# if 1:    #
#     pass


# 사칙연산.
# +, -, *,**, /, //, %
# % -> 배수 판별 , 짝홀 판별


aAge, aSex = map(str, input().split())

aAge = int(aAge)


y = int(input())

# y 가 윤년인지?
# 윤년이 뭐야?
# 윤년은 4의 배수 -> %
# 만약 4의 배수 and


# 몇월 몇 일 있니?

# 31,        - 홀수
#     28,    - 짝수 and 2
# 31,        - 홀수
#     30,    - 짝수
# 31,        - 홀수
#     30,    - 짝수
# 31,        - 홀수

# 31,        - 짝수
#    30,     - 홀수
# 31,        - 짝수
#    30,     - 홀수
# 31,        - 짝수


# if n >= 8
# if n 이짝수라면?
#       31

# else:

# if n 이홀수라면?
#       31
# else :
# 30


######################
# 논리적 사고 !
# 배타적인 사고,, (이분법적으로 생각)
# 남자 + 여자 :
# 남자 ,여자 -> If 남자가 아니라면 -> 여자 !
# 남자 ,여자 -> If 여자가 아니라면 -> 남자 !

# 양의정수는 2가지로 ,,, -> 짝수,홀수
# 어떤 양의정수가 짝수가아니래 ,, -> 홀수
# 어떤 양의정수가 홀수가아니래 ,, -> 짝수

# A,B,C,D,F
# 8 명


# A ,M/W: 3
# B ,M/W: 2
# C ,M/W: 3


# if A :
#    if W/M
# elif B:
#    if W/M
# else:
#   if W/M


# 가장 밖에서 잡아주는거야

# 1 2 3 -> 3
# 1 3 3 -> 3
# 3 3 3 -> 3

# if a>=b and a>=c
