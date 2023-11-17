
# 출력 : print() / [내장]함수 / 실행 : ()
#   옵션 : end ="\n"
#   옵션 : sep =" "

# 입력 : input() / [내장]함수 / 실행 : () / str
#    한개 씩 만 입력을 받았어
#   여러개 받고 싶어서 묶어주었어 -> map()


# 초기화

# 자료형
# 숫자(int, float), 문자(str)

# int : 딱 떨어진는 수 : 5
# float : 5.0

# str
# "문자" + "열"
# 문자열 = 문자열 + 문자열

# 12 + 23 35
# "12"+"23" 1223

print("40")
print(30, 60)


print("40", 30, sep=" ", end="\n")

print(4 + 5 + 1 + 10)  # 하나만

print(4 + 5, "hi" + "bye")
print(9, "hibye")

# 값 -> Print(값,값,값,값) -> 출력


# 문제 : print 함수 하나를 사용해서

# print(1, "+" ,2)
#     인자 : 3개
#     int , str , int

# print(1 + 2) :X

a = 123456666788900000147182456

print("a is", a, " ,GOOD!")
# str , int , str
print(f"a is {a}  ,GOOD!")  # 포매팅기능을 추가하는 것 : 이걸하면 ? 문자열 안에 변수를 쓸수 있어요
# str

# 형변환
# print(값)
# int(값)
# type(값)

num = "123"  # str
print(type(num), num)

num = int("123")  # int
print(type(num), num)

num = str(int("123"))  # str
print(type(num), num)


a = 25

b = a + a
# b|_a+a_|
print(b)

b = a + a
# b|_a+a_|
print(b)

a = 25 + 25
# a|_25+25_|
print(b)

a = 25 + 25 + 25 + 25
# a|_25+25+25+25_|
print(a)

# a : 10 b : 20
# "a + b = c"
# int, str, int, str, int
c = 30

print(f"{a} + {b} = {c}")
d = 3.141592

print("%.5f" % d)
print("%.4f" % d)
print("%.3f" % d)
print("%.2f" % d)
print("%.1f" % d)
print("%1.f" % d)
print("%2.f" % d)
print("%3.f" % d)
print("%4.f" % d)
print("%5.f" % d)

# # _ _ _._ _
