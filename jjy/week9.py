# # map split

# # 21 7 33 한 줄에 입력

# # input() -> str -> "21 7 33"


# a, b, c = input().split(" ")
# a, b, c = "21 7 33".split(" ")
# a, b, c = "21", "7", "33"

# # map
# a, b, c = map(int, input().split(" "))
# a, b, c = map(int, "21 7 33".split(" "))
# a, b, c = map(int, "21", "7", "33")
# a, b, c = int("21"), int("7"), int("33")
# a, b, c = 21, 7, 33

# 나는 달린다.
# 나는 빠르게.
# 나는 빠르게 달린다.

# 여러가지연산 / !,~ not
# + , - , * , / (진짜 나누기) , //(몫 나누기) , % (나머지 나누기)
# == (같다)
# != (다르다)
# <,> (크,작다)
# <=,>=

# 불(참거짓)형 : 1 >= 0
# print(1 >= 0)

# % (나머지 나누기)
# 짝수 홀수 구분하기
# 짝수: 2로 나누었을 때 나머지 0 인 수
# 7 % 2 == 0

# % (나머지 나누기)
# k 배수 인지 ?
# 6 % 3 == 0
# print(151894125 % 15 == 0)

# 자리수에 수를 한정할 수 있다.

# 1의 자리수 ?
# 12946912 % 10

# 10의 자리수 ?
# (12946912 % 100)//10
# 12//10

# 100의 자리수 ?
# (12946912 % 1000)//100
# 912//100


a = 2
b = 7

# 손이 하나일 때
# a 의 값이 사라져 !
temp = a
a = b
b = temp

# 손이 둘일 때
a, b = b, a


# res = a,b #튜플

# 변수(주소) = 데이터 값

print(a, b, 231, sep="+")
# 구분할꺼니
# sep = " "
# end ="\n"

# res
# %
# print("%.2f" % res)
