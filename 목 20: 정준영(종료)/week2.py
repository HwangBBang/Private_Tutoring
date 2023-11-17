# 변수와 초기화

# 변수 생성
# 필요한것 : 변수명 , 변수의 값

# 주소의 별명 = 값


import tkinter
number = 3  # (O)
num_3 = number  # (O)
# print(number, num_3)
# 3 = number (X)
# | 변수명(주소) |  =  | 값 |

# 변수에 값을 세팅하는 것을 " 초기화 " 라고한다.

cat_age = 4  # 초기화 ,선언 , 할당
# cat_age 의 값 4이야
# print(f"cat age is {cat_age}")
# cat_age 의 값 4이야

cat_age = 5
# cat_age 의 값 5이야
# print(f"cat age is {cat_age}")
# cat_age 의 값 5이야

cat_age = cat_age+1
# cat_age 의 값 6이야

cat_hair = 14123412341234213213
# cat_hair = 14123412341234213213 - 500
cat_hair = cat_hair - 500
# --------------------------------------------
# 자료형(type)

# 숫자 : 11 , 문자 : 11

num_i = 11
num_s = "11"

# print(type(num_i), num_i, end="\n")
# print(type(num_s), num_s)

# 숫자, 문자

# 숫자 (정수, 실수)
# - 정수 : int eger  (소수점이 있는지 ? 없는지 ?)
# 양의 정수 ,0 ,음의 정수
# 양의 정수 : 3,7,1,314
# 음의 정수 : -3,-7,-1,-314

# - 실수 : float
# 양의 실수 : 31.10
# 음의 실수 : -31.10

# 문자
# - 문자열 : str ing
# 문자열 : ": 문자열 시작합니다. / ": 문자열 끝납니다.
# 문자열 : ': 문자열 시작합니다. / ': 문자열 끝납니다.
# 문자열 : """: 문자열 시작합니다. / """: 문자열 끝납니다.
# 문자열 : ''': 문자열 시작합니다. / ''': 문자열 끝납니다.

# 문자열 = 문자열 + 문자열
# "a" : str (문자열)
# "aa" : str (문자열)
# "aa" = "a" + "a"
str_1 = "a" + "a"
str_2 = "aa"
print(str_1 + str_1)
# "a" + "a" + "a" + "a"
print(str_2 + str_1)


# <Quiz>
# 31     : int
# 31.1   : float
# "31.1" : str
# 0.0    : float
# 1.0    : float
# 0      : int
# "0"    : str
# "ppp"  : str
# 2315415125341 : int
# -1424 : int
# 3.1415926278 : float
# "sa31" : str
# "" : str
# " " : str

print("3145154 13's " + '"adqw21e12"')
print("3145154 13's \"adqw21e12\" ")

print("""3145154 13's "ad+qw2/1e12 """)


# 시나리오, 장르
# 프로토타입

# 깃허브 사용법
# 클래스개념 맴버 개념
# 파이게임 으로 오브젝트 움직이기

# 예제 토대로 게임을 만들어

# 라이브러리
# 함수 ,OOP ,리팩토링 X -> 유지
# 변수
