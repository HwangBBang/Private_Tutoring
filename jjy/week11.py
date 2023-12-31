# set 초기화 , 타입

#

a = 1
# & =
# a|_1_|
a = 5
# a|_5_|
b = 7


# a <-> b
a, b = 5, 7
a = 5
b = 7

# 한번에 바꾼다고 .
a, b = b, a

print(a, b)
# python


# a = int(input())
# a = int("2 7 6")   # 하나.딱.
"2 7 6".split(" ")

["2", "7", "6"]

# map  배열의 원소들 모두에게 어떤 동작을 적용시키는 것

# () -> 동작 -> ()


def addOne(inputNum):
    inputNum = inputNum+1
    return inputNum


a1, a2, a3 = map(int, ["2", "7", "6"])
print(type(a1), a1, type(a2), a2, type(a3), a3)

a1, a2, a3 = map(addOne, [a1, a2, a3])
print(type(a1), a1, type(a2), a2, type(a3), a3)
# time_two
# timeTwo
# input()

# def funName(parameter):


# f(x) = x+1

# + - * /진짜 //몫 %나머지

# def f1(n):
#     a = n % 10
#     return a

# num = int(input())

# print(f1(num))

# 생각. 문제 태도 질문

# 짝수
# 1의 자리수

# 타입. 내가 필요한 정보.
# str , 2개 .
"2" "1"
# 초기화 : =
print(sep="")

# "1 3" -> "1" ,"3"
# str
# a, b = "1", "3"

# int , 1개만 됩니다.-------->


# res1 =
# res2 =
# res3 =
# res4 =
# sep


# a, b = input().split(" ")
# a = int(a)
# b = int(b)

w, h = map(int, input().split(" "))

w = w+8
h = h*3

# 변수가 많아지면.. 헷갈려..
# 값을 업데이트 즉, 의미 같은 녀석은 변수를 "재활용"
