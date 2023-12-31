# 반복문
# for 반복하기
# while 반복하기

# break : 반복문을 깨부신다.
# continue : 아래를 생략하고, 즉시 조건을 확인해


# [10] for i in range(0,10,1)
# [10] for i in range(10,0,-1)
# [10] for _ in range(10) 단순 반복일 때

# for i in range(10, 0, -1):
# print(123)


# while con:
# code
#

# if con:    조건문, 분기문
# code


# cnt = 0  # cnt : 0

# for _ in range(10):
#     a = int(input())
#     if a % 2 == 1:
#         cnt += 1


# ["2","2","3" ..]
# "223123231" string 문자(배)열

# "21 13 7"
a, b, c = input().split(" ")
a, b, c = "21 13 7".split(" ")
a, b, c = "21 ", "13 ", "7"
a, b, c = int(a), int(b), int(c)

# "21 13 7"
a, b, c = int(input()).split(" ")
a, b, c = int("21 13 7").split(" ")

# "21 13 7"
a, b, c = int(input().split(" "))
a, b, c = int("21 13 7".split(" "))
a, b, c = int("21", "13", "7")

a, b, c = map(int, input().split(" "))
a, b, c = map(int, "21 13 7".split(" "))
a, b, c = map(int, "21", "13", "7")
a, b, c = int("21"), int("13"), int("7")
a, b, c = 21, 13, 7

# input() 함수 / split() 메서드

# 나는 입력받아 . (O)
# 나는 구분해서 . (X)
# 나는 구분해서 입력받아 . (O)


# 날짜
cnt_0 = 0  # 교실
cnt_1 = 0  # 복도
cnt_2 = 0  # 화장실

# "%.1f" %avr
