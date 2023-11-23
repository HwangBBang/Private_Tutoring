# print(),input() 함수
# end = "\n" new line
# sep = " " , 여러 인자들을 (어떻게???)구분해 출력 !

# id = input("ID :")
# print("id는 ", id)

# type(자료형) : int(정수) , str(문자열) , float(실수) , bool(불)

# input() 함수 -> 리턴 자료형 str  -> 형 변환 -> 타입으로 감싸주세요 int("99")

# map() , .split()

# 여러개 한 줄에 입력 받기
# map(type , input().split())

# 분기 , 조건문

# if  - elif - else
#  : , 들여쓰기 (인덴트)
# g = 99

# if g == 100:
#     print("GOOD")
# elif g == 90:
#     print("SOSO")

# for , while
# for 범위나 정도를 알 때요

# for i in range(9):
#     print("hi", end=" ")

# while condition:
#    continue
#   if 반복을 4번했으면 :
#      break

# + , - , * , / , // , % , **
# == , != , > , < , <= , >=

# %
# 짝수 홀수 , n배수 , n의 자리수

# 1의 자리수 : (19546 % 10)//1
# 10의 자리수 : (19546 % 100)//10
# 100의 자리수 : (19546 % 1000)//100
# 1000000의 자리수 : (115983719579546 % 10000000)//1000000

# if 분기 .. 경우의 수 분류

# "%.1f" %avg
# 28 1 2 4 7 14
def isNum(n):
    sum1 = 0
    for i in range(1, n):
        if n % i == 0:
            sum1 += i

    if sum1 == n:
        print(f'{n}은 완전수')


# 나 = 약수들의 합이야..(나는 빼고~)
for j in range(1, 10000):
    isNum(j)
# 나누어 떨어지는 수들의 집합
