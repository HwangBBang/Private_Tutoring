# # 숫자랑 문자 .
# # print(end = "\n" ,sep = " ") 함수 ,

# # 자료형
# # int, str, float
# # 3.0
# # 231 + 231 = 462
# # "231" + " 231" = "231 231"

# # input() / 터미널 -> 소스삽입
# # 하나만 딱 입력 가능.
# # type : str
# # str 숫자도 입력받고 싶어
# # 형변환
# # int(input()), float(input())

# def change_9(num):
#     num = 9
#     return 9

# add_one 이라는 함수 정의함
# 매개변수로 num 을 받아 .
# num ---> add_one ---> num+1 (리턴)
# : 헤더문에는 인덴트를 꼭줘야해

def add_one(num):
    num += 1
    return num


# # def input(dad):
# #     return "입력받은~"


# # 34 ----> change_9 ----> 9
# change_9(34)

# # input() # 하나밖에 입력을 못했어.
# # 한 줄에 여러개를 입력하는 효과를 내고싶어
# "33:22:11"
# input().split(":")
# "33", "22", "11"
# int("33"), int("22"), int("11")
# map 여러 요소들에게 동일한 동작을 시켜요

# X = [1, 2, 3, 4]
#  map(int ,input().split())

# a, b, c, d = map(add_one, X)
# print(a, b, c, d)

# map(각각의 원소들에게 적용할 함수 , 원소들의 뭉치)
# 함수를 *3하는 함수 리턴은 연산 값을 리턴하세요

# 입력을 받으세요 한줄에요

# 정수변환과 *3함수를 map 시켜서

# a,b,c 결과를 출력하세요

# arr = [a,b,c]
